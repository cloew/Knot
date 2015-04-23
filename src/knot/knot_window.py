from knot.dimensions import HORIZONTAL, VERTICAL
from knot.events.event_types import WIDGET_CREATED
from knot.core.sizing.stretch import Stretch

from .knot_body import KnotBody
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
        self.centralWidget = KnotBody()
        self.centralWidget.parent = self
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
        if child.widgetType in ['body', 'menu-bar', 'status-bar']:
            super().addChild(child)
        else:
            self.centralWidget.addChild(child)
    
    def setCentralWidget(self, widget=None, event=None):
        """ Set the central widget of the window """
        self.centralWidget.draw()
        self._qwidget.setCentralWidget(self.centralWidget._qwidget)
        
    def printChildren(self, parent=None, event=None):
        """ """
        if parent is None:
            parent = self
        for child in parent.children:
            print(child, child.geometry())
            self.printChildren(parent=child)