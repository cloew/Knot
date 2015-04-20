from knot.events.event_types import PARENT_ADDED, WIDGET_CREATED

from kao_decorators import lazy_property

from PySide.QtGui import QStatusBar

class StatusBarController:
    """ Handles the attachment of the status bar to the window """
        
    def attachWidget(self, widget):
        """ Attach to the widget """
        self.widget = widget
        self.widget.on(PARENT_ADDED, self.trackParent)
        
    def trackParent(self, widget=None, event=None):
        """ Track the parent widget """
        self.widget.parent.on(WIDGET_CREATED, self.connectToParentQWidget)
        
    def connectToParentQWidget(self, widget=None, event=None):
        """ Connect to the parent signal """
        self.widget.parent._qwidget.setStatusBar(self.statusBar)
        self.widget.setQWidget(self.statusBar, ignoreParent=True)
        
    def displayContextMenu(self, point):
        """ Display the context menu """
        globalPoint = self.widget.parent._qwidget.mapToGlobal(point)
        self.menu.exec_(globalPoint)
       
    @lazy_property
    def statusBar(self):
        """ Return the status bar """
        return QStatusBar()