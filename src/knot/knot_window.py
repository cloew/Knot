from .widget import Widget
from .events.event_types import *
from .loader.factory.widget_factory import WidgetFactory

from .core.painters.window_painter import WindowPainter
from .core.positioning.center import Center
from .core.sizing.stretch import Stretch

from kao_decorators import proxy_for

@proxy_for('_qwidget', ['setWindowTitle'])
class KnotWindow(Widget):
    """ Represents the window the knot elements will be rendered in """
    
    def __init__(self):
        """ Initialize the window """
        Widget.__init__(self, WindowPainter(''))
        # self.div = WidgetFactory.build('div', "", positioning=Center(), sizing=Stretch())
        # self.addChild(self.div)
        
        # self.label1 = WidgetFactory.build('text', "Some Text")
        # self.div.addChild(self.label1)
        # self.label2 = WidgetFactory.build('text', "Some Other Text", sizing=Stretch())
        # self.div.addChild(self.label2)
        # self.label3 = WidgetFactory.build('text', "EVEN MORE TEXT!!!!!!")
        # self.div.addChild(self.label3)
        
        # self.label2.on(RESIZED, self.printSomething)
        
    def printSomething(self, div, event):
        print("Inside event")
        print(event)
        print(self.div, self.div._qwidget.geometry())
        print(self.label1, self.label1._qwidget.geometry())
        print(self.label2, self.label2._qwidget.geometry())
        print(self.label3, self.label3._qwidget.geometry())