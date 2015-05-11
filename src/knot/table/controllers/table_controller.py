from knot import KnotService
from knot.events.event_types import CHILD_ADDED, WIDGET_CREATED

from .knot_table_model import KnotTableModel

class TableController:
    """ Controller to handle managing a table """
    app = KnotService('app')
    
    def __init__(self):
        """ Initialize the controller """
        self._columns = []
        
    def attachWidget(self, widget):
        """ Attach the widget """
        self.widget = widget
        widget.on(WIDGET_CREATED, self.addModelOnQCreation)
        widget.on(CHILD_ADDED, self.trackColumns)
        
    def addModelOnQCreation(self, widget, event=None):
        """ Add Table model to the table widget """
        tableModel = KnotTableModel([column.controller for column in self._columns])
        self.widget._qwidget.setModel(tableModel)
        self.widget._qwidget.resizeColumnsToContents()
        
    def trackColumns(self, widget=None, event=None):
        """ Track the columns """
        columns = self.widget.getChildrenWithType('column')
        newColumns = [column for column in columns if column not in self._columns]
        
        for column in newColumns:
            self._columns.append(column)