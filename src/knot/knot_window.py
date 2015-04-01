from knot.dimensions import HORIZONTAL, VERTICAL
from .widget.widget import Widget

from .core.painters.window_painter import WindowPainter

from kao_decorators import proxy_for

@proxy_for('_qwidget', ['setWindowTitle', 'windowTitle'])
class KnotWindow(Widget):
    """ Represents the window the knot elements will be rendered in """
    
    def __init__(self, title=''):
        """ Initialize the window """
        Widget.__init__(self, WindowPainter(''))
        self.title = title
        
    def draw(self, *args, **kwargs):
        """ Draw the widget """
        Widget.draw(self, *args, **kwargs)
        self._setWindowTitle()
        
    def printChildren(self, parent=None, event=None):
        """ """
        if parent is None:
            parent = self
        for child in parent.children:
            print(child, child._qwidget.geometry())
            self.printChildren(parent=child)
            
    @property
    def title(self):
        """ Return the title """
        return self.windowTitle() if self.hasQWidget() else self.__title
        
    @title.setter
    def title(self, value):
        """ Set the title """
        self.__title = value
        self._setWindowTitle()
        
    def _setWindowTitle(self):
        """ Set the title on the window """
        if self.hasQWidget():
            self.setWindowTitle(self.__title)