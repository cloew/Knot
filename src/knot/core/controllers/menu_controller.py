from knot.events.event_types import PARENT_ADDED, WIDGET_CREATED

from kao_decorators import lazy_property

from PySide.QtGui import QMenu

class MenuController:
    """ Handles adding a menu to a parent menu """
        
    def attachWidget(self, widget):
        """ Attach to the widget """
        self.widget = widget
        self.widget.on(PARENT_ADDED, self.addMenuToParent)
        
    def addMenuToParent(self, widget=None, event=None):
        """ Track the parent widget """
        self.parentMenu.addMenu(self.menu)
        
    @property
    def parentMenu(self):
        """ Return the parent menu """
        return self.widget.parent.controller.menu
        
    @lazy_property
    def menu(self):
        """ Return the current menu """
        return QMenu(self.menuTitle)
        
    @property
    def menuTitle(self):
        """ Return the title for the menu """
        return self.widget.content.text if self.widget.content is not None else ''