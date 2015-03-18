from .widget import Widget
from .widget_factory import BuildWidget

from .core.painters.window_painter import WindowPainter
from .core.positioning.center import Center
from .core.sizing.shrink_to_contents import ShrinkToContents
from .core.sizing.use_size_hint import UseSizeHint

from kao_decorators import proxy_for

@proxy_for('_qwidget', ['setWindowTitle'])
class KnotWindow(Widget):
    """ Represents the window the knot elements will be rendered in """
    
    def __init__(self):
        """ Initialize the window """
        Widget.__init__(self, WindowPainter(''))
        self.div = BuildWidget('div', "", sizing=ShrinkToContents())
        self.div.positioning = Center()
        self.addChild(self.div)
        
        self.div.addChild(BuildWidget('text', "Some Text", sizing=UseSizeHint()))
        self.div.addChild(BuildWidget('text', "Some Other Text", sizing=UseSizeHint()))
        self.label3 = BuildWidget('text', "EVEN MORE TEXT!!!!!!", sizing=UseSizeHint())
        self.div.addChild(self.label3)
        
    def printSomething(self, div, event):
        print("Inside event")
        print(self.div, div)
        print(event)