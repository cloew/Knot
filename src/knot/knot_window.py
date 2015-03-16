from .widget import Widget
from .widget_factory import BuildWidget

from .core.painters.window_painter import WindowPainter

from kao_decorators import proxy_for

@proxy_for('_qwidget', ['setWindowTitle'])
class KnotWindow(Widget):
    """ Represents the window the knot elements will be rendered in """
    
    def __init__(self):
        """ Initialize the window """
        Widget.__init__(self, WindowPainter(''))
        self.addChild(BuildWidget('text', "Some Text"))
        self.addChild(BuildWidget('text', "Some Other Text"))
        self.addChild(BuildWidget('text', "EVEN MORE TEXT!!!!!!"))