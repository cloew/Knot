from knot.events.event_types import PARENT_ADDED, WIDGET_CREATED

from kao_decorators import lazy_property

from PySide.QtGui import QMenuBar

class MenuBarController:
    """ Handles the attachment of a menu bar to the parent window """
        
    def attachWidget(self, widget):
        """ Attach to the widget """
        self.widget = widget
        self.widget.on(PARENT_ADDED, self.trackParent)
        
    def trackParent(self, widget=None, event=None):
        """ Track the parent widget """
        self.widget.parent.on(WIDGET_CREATED, self.addMenuBar)
        
    def addMenuBar(self, widget=None, event=None):
        """ Add the menu bar """
        self.widget.parent._qwidget.setMenuBar(self.menu)
       
    @lazy_property
    def menu(self):
        """ Return the current menu """
        return QMenuBar()