from knot.events.event_types import CHILD_ADDED, WIDGET_CREATED

class TabViewController:
    """ Controller to handle mapping Tabs """
    
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
        self.widget._qwidget.addTab(tab._qwidget, tab.controller.label)
        
    def trackChildTab(self, widget=None, event=None):
        """ Track the child tab records """
        tabs = self.widget.getChildrenWithType('tab')
        newTabs = [tab for tab in tabs if tab not in self._tabs]
        
        for tab in newTabs:
            self._tabs.append(tab)
            if self.widget.canMove():
                self.addTab(tab)