from knot import KnotService
from knot.events.event_types import CHILD_ADDED, WIDGET_CREATED

class TableController:
    """ Controller to handle managin a table """
    app = KnotService('app')
    
    def __init__(self):
        """ Initialize the controller """
        self._columns = []
        
    def attachWidget(self, widget):
        """ Attach the widget """
        self.widget = widget
        widget.on(WIDGET_CREATED, self.addColumnsOnQCreation)
        widget.on(CHILD_ADDED, self.trackColumns)
        
    def addColumnsOnQCreation(self, widget, event=None):
        """ Add actual columns to the table widget """
        for column in self._columns:
            self.addColumn(column)
        
    def addColumn(self, column):
        """ Add the column to the underlying QTableWidget """
        column.draw()
            
        # self.app.watch(tab, 'controller.label', updateTabLabel)
        self.widget._qwidget.setColumnCount(len(self._columns))
        
    def trackColumns(self, widget=None, event=None):
        """ Track the columns """
        columns = self.widget.getChildrenWithType('column')
        newColumns = [column for column in columns if column not in self._columns]
        
        for column in newColumns:
            self._columns.append(column)
            if self.widget.canMove():
                self.addColumn(column)