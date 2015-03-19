from .widget import Widget
from .loader.factory.widget_factory import WidgetFactory

from .core.painters.window_painter import WindowPainter
from .core.positioning.center import Center

from kao_decorators import proxy_for

@proxy_for('_qwidget', ['setWindowTitle'])
class KnotWindow(Widget):
    """ Represents the window the knot elements will be rendered in """
    
    def __init__(self):
        """ Initialize the window """
        Widget.__init__(self, WindowPainter(''))
        # self.div = WidgetFactory.build('div', "", positioning=Center())
        # self.addChild(self.div)
        
        # self.div.addChild(WidgetFactory.build('text', "Some Text"))
        # self.div.addChild(WidgetFactory.build('text', "Some Other Text"))
        # self.label3 = WidgetFactory.build('text', "EVEN MORE TEXT!!!!!!")
        # self.div.addChild(self.label3)
        
    def printSomething(self, div, event):
        print("Inside event")
        print(self.div, div)
        print(event)