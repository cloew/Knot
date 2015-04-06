from .positioning_handler import PositioningHandler
from .qt_handler import QtHandler
from .sizing_handler import SizingHandler
from .tree_handler import TreeHandler
from ..events.event_handler import EventHandler

from knot.core.painters.container_painter import ContainerPainter

from kao_decorators import proxy_for
from smart_defaults import smart_defaults, EvenIfNone, PerCall

@proxy_for('_qwidget', ['resize', 'show', 'sizeHint'])
@proxy_for('eventHandler', ['fire', 'on', 'unregister'])
@proxy_for('positioningHandler', ['apply', 'getDefaultChildrenPolicies', 'getSidePosition', 'getInternalSidePosition', 'setSidePosition'])
@proxy_for('qtHandler', ['hasQWidget', 'setQWidget', 'setContent', '_qwidget'])
@proxy_for('sizingHandler', ['apply', 'resizeWithPolicies'])
@proxy_for('treeHandler', ['parent', 'children', 'siblings', 'addChild', 'attachToParent', 'getSiblingOn', 'getPreviousSibling'])
class Widget:
    """ Represents a widget within Knot """
    
    @smart_defaults
    def __init__(self, painter=EvenIfNone(ContainerPainter()), controller=None, mods=PerCall([]), positioning=None, sizing=None):
        """ Initialize the widget with its painters and policies """
        self.controller = controller
        self.painter = painter
        self.mods = mods
        self.eventHandler = EventHandler(self)
        self.treeHandler = TreeHandler(self)
        self.positioningHandler = PositioningHandler(self, policy=positioning)
        self.sizingHandler = SizingHandler(self, sizing)
        self.qtHandler = QtHandler(self)
        
        thingsToAttach = self.mods if self.controller is None else [self.controller] + self.mods
        for thing in thingsToAttach:
            if hasattr(thing, 'attachWidget'):
                thing.attachWidget(self)
        
    def draw(self):
        """ Draw the widget given its parent """
        self.painter.draw(self)
        
    def canMove(self):
        """ Return if this widget can move """
        return self.hasQWidget()
        
    @property
    def height(self):
        """ Return the widget's height """
        return self._qwidget.height()
        
    @property
    def width(self):
        """ Return the widget's width """
        return self._qwidget.width()
        
    @property
    def left(self):
        """ Return the widget's left x coordinate """
        return self._qwidget.x()

    @left.setter
    def left(self, value):
        self._qwidget.move(value, self.top)
        self._qwidget.show()
        
    @property
    def right(self):
        """ Return the widget's right x coordinate """
        return self.left + self.width

    @right.setter
    def right(self, value):
        self._qwidget.move(value-self.width, self.top)
        self._qwidget.show()
        
    @property
    def top(self):
        """ Return the widget's top y coordinate """
        return self._qwidget.y()

    @top.setter
    def top(self, value):
        self._qwidget.move(self.left, value)
        self._qwidget.show()
        
    @property
    def bottom(self):
        """ Return the widget's bottom y coordinate """
        return self._qwidget.y() + self.height

    @bottom.setter
    def bottom(self, value):
        self._qwidget.move(value-self.height, self.top)
        self._qwidget.show()
