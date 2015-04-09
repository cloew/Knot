from .base_widget import BaseWidget
from .container_handler import ContainerHandler
from .policies_handler import PoliciesHandler
from .positioning_defaults_provider import PositioningDefaultsProvider
from .qt_handler import QtHandler
from .sizing_defaults_provider import SizingDefaultsProvider
from .style_handler import StyleHandler

from knot.sides import LEFT, RIGHT, TOP, BOTTOM
from knot.core.painters.container_painter import ContainerPainter

from kao_decorators import proxy_for
from smart_defaults import smart_defaults, EvenIfNone, PerCall

@proxy_for('_qwidget', ['resize', 'show', 'sizeHint'])
@proxy_for('containerHandler', ['direction', 'setDirection', 'getDefaultChildrenPolicies', 'getContainerSidePosition'])
@proxy_for('qtHandler', ['hasQWidget', 'setQWidget', 'setContent', 'setValue', 'getValueSignal', '_qwidget'])
class Widget(BaseWidget):
    """ Represents a widget within Knot """
    
    @smart_defaults
    def __init__(self, widgetType, content=None, painter=EvenIfNone(ContainerPainter()), controller=None,
                       mods=PerCall([]), positionings=None, sizings=None, styling=EvenIfNone('')):
        """ Initialize the widget with its painters and policies """
        self.painter = painter
        self.containerHandler = ContainerHandler(self)
        BaseWidget.__init__(self, widgetType, content=content, controller=controller, mods=mods)
        
        self.positioningDefaults = PositioningDefaultsProvider(self)
        self.positioningHandler = PoliciesHandler(self, self.positioningDefaults, policies=positionings)
        self.sizingHandler = PoliciesHandler(self, SizingDefaultsProvider(self), policies=sizings)
        self.styleHandler = StyleHandler(self, styling)
        self.qtHandler = QtHandler(self)
        
    def draw(self):
        """ Draw the widget """
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
        
    def getSidePosition(self, side):
        """ Return the pixel position of the given side """
        if side is LEFT:
            return self.left
        elif side is RIGHT:
            return self.right
        elif side is TOP:
            return self.top
        elif side is BOTTOM:
            return self.bottom
        
    def setSidePosition(self, side, value):
        """ Set the pixel position of the given side """
        if side is LEFT:
            self.left = value
        elif side is RIGHT:
            self.right = value
        elif side is TOP:
            self.top = value
        elif side is BOTTOM:
            self.bottom = value
            
    def resizeWithPolicies(self):
        """ Resize the widget """
        [policy.resize(self) for policy in self.sizingHandler.policies]