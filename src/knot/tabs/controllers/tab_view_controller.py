from knot import KnotService
from knot.events.event_types import CHILD_ADDED, WIDGET_CREATED

class TabViewController:
    """ Controller to handle mapping Tabs """
    app = KnotService('app')
    
    def __init__(self):
        """ Initialize the controller """
        self._tabs = []
        
    def attachWidget(self, widget):
        """ Attach the widget """
        self.widget = widget
        widget.on(WIDGET_CREATED, self.addTabsOnQCreation)
        widget.on(CHILD_ADDED, self.trackChildTab)
        
    def addTabsOnQCreation(self, widget, event=None):
        """ Attach the signal to the qt signal and the watch to the application """
        for tab in self._tabs:
            self.addTab(tab)
        
    def addTab(self, tab):
        """ Add the tab to the underlying QTabWidget """
        tab.draw()
        
        def updateTabLabel(value):
            self.widget._qwidget.setTabText(self._tabs.index(tab), value)
            
        self.app.watch(tab, 'controller.label', updateTabLabel)
        self.widget._qwidget.addTab(tab._qwidget, tab.controller.label)
        
    def trackChildTab(self, widget=None, event=None):
        """ Track the child tab records """
        tabs = self.widget.getChildrenWithType('tab')
        newTabs = [tab for tab in tabs if tab not in self._tabs]
        
        for tab in newTabs:
            self._tabs.append(tab)
            if self.widget.canMove():
                self.addTab(tab)