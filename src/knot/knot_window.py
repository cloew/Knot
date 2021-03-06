from knot.dimensions import HORIZONTAL, VERTICAL
from knot.events.event_types import WIDGET_CREATED
from knot.core.sizing.stretch import Stretch

from .knot_body import KnotBody, window_widgets
from .widget.widget import Widget

from .core.painters.window_painter import WindowPainter

from kao_decorators import proxy_for

@proxy_for('_qwidget', ['setWindowTitle', 'windowTitle'])
class KnotWindow(Widget):
    """ Represents the window the knot elements will be rendered in """
    
    def __init__(self, title=''):
        """ Initialize the window """
        Widget.__init__(self, 'window', painter=WindowPainter(''))
        self.title = title
        self.body = KnotBody()
        self.body.parent = self
        self.on(WIDGET_CREATED, self.onQWidgetCreated)
            
    @property
    def title(self):
        """ Return the title """
        return self.windowTitle() if self.hasQWidget() else self.__title
        
    @title.setter
    def title(self, value):
        """ Set the title """
        self.__title = value
        self._setWindowTitle()
        
    def onQWidgetCreated(self, widget=None, event=None):
        """ Update the QWidget """
        self._setWindowTitle()
        self.setCentralWidget()
        
    def _setWindowTitle(self):
        """ Set the title on the window """
        if self.hasQWidget():
            self.setWindowTitle(self.__title)
            
    def addChild(self, child):
        """ Add the child """
        if child.widgetType in window_widgets:
            super().addChild(child)
        else:
            self.body.addChild(child)
    
    def setCentralWidget(self, widget=None, event=None):
        """ Set the central widget of the window """
        self.body.draw()
        self._qwidget.setCentralWidget(self.body._qwidget)
        
    def printChildren(self, parent=None, event=None):
        """ """
        if parent is None:
            parent = self
        for child in parent.children:
            print(child, child.geometry())
            self.printChildren(parent=child)