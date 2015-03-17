
from kao_decorators import proxy_for

@proxy_for('_qwidget', ['show'])
class Widget:
    """ Represents a widget within Knot """
    
    def __init__(self, painter):
        """ Initialize the widget with its painters """
        self.painter = painter
        self.children = []
        self.parent = None
        
    def draw(self):
        """ Draw the widget given its parent """
        self.painter.draw(self)
        
    def addChild(self, child):
        """ Add the Child to this widget """
        self.children.append(child)
        child.parent = self
        
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