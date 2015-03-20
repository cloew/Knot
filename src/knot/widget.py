from .core.positioning.from_neighbor import FromNeighbor
from .events.event_handler import EventHandler
from .events.event_types import CHILD_ADDED

from kao_decorators import proxy_for
from smart_defaults import smart_defaults, EvenIfNone, PerCall

@proxy_for('_qwidget', ['resize', 'show', 'sizeHint'])
@proxy_for('eventHandler', ['on', 'unregister'])
class Widget:
    """ Represents a widget within Knot """
    
    @smart_defaults
    def __init__(self, painter, mods=PerCall([]), positioning=EvenIfNone(PerCall(FromNeighbor())), sizing=None):
        """ Initialize the widget with its painters """
        self.painter = painter
        self.children = []
        self.parent = None
        self.mods = mods
        self.eventHandler = EventHandler(self)
        self.positioning = positioning
        self.sizing = sizing
        self._qwidget = None
        
    def setQWidget(self, qwidget):
        """ Set the underlying Qt Widget for this widget """
        self._qwidget = qwidget
        self.eventHandler.attachEvents(qwidget)
        
    def draw(self):
        """ Draw the widget given its parent """
        self.painter.draw(self)
        [mod.afterDraw(self) for mod in self.mods]
        
    def addChild(self, child):
        """ Add the Child to this widget """
        self.children.append(child)
        child.attachToParent(self)
        self.eventHandler.fire(CHILD_ADDED, event=child)
        
    def attachToParent(self, parent):
        """ Add the Child to this widget """
        self.parent = parent
        self.positioning.applyToWidget(self)
        if self.sizing is not None:
            self.sizing.applyToWidget(self)
        
    @property
    def siblings(self):
        """ Return the given widget's siblings """
        return [child for child in self.parent.children if child is not self]
            
    def canMove(self):
        """ Return if this widget can move """
        return self._qwidget is not None
        
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
