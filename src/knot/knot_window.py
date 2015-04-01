from knot.dimensions import HORIZONTAL, VERTICAL
from .widget.widget import Widget

from .core.painters.window_painter import WindowPainter

from kao_decorators import proxy_for

@proxy_for('_qwidget', ['setWindowTitle'])
class KnotWindow(Widget):
    """ Represents the window the knot elements will be rendered in """
    
    def __init__(self):
        """ Initialize the window """
        Widget.__init__(self, WindowPainter(''))
        
    def printChildren(self, parent=None, event=None):
        """ """
        if parent is None:
            parent = self
        for child in parent.children:
            print(child, child._qwidget.geometry())
            self.printChildren(parent=child)