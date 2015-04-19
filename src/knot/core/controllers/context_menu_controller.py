from knot.events.event_types import PARENT_ADDED, WIDGET_CREATED

from kao_decorators import lazy_property

from PySide.QtCore import Qt
from PySide.QtGui import QMenu

class ContextMenuController:
    """ Handles the management of a Right-Click Context Menu """
    
    def __init__(self):
        """ Initialize the Context Menu Controller """
        
    def attachWidget(self, widget):
        """ Attach to the widget """
        self.widget = widget
        self.widget.on(PARENT_ADDED, self.trackParent)
        
    def trackParent(self, widget=None, event=None):
        """ Track the parent widget """
        self.widget.parent.on(WIDGET_CREATED, self.connectToParentQWidget)
        
    def connectToParentQWidget(self, widget=None, event=None):
        """ Connect to the parent signal """
        self.widget.parent._qwidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.widget.parent._qwidget.customContextMenuRequested.connect(self.displayContextMenu)
        
    def displayContextMenu(self, point):
        """ Display the context menu """
        globalPoint = self.widget.parent._qwidget.mapToGlobal(point)
        self.menu.exec_(globalPoint)
       
    @lazy_property
    def menu(self):
        """ Return the current menu """
        return QMenu()