from knot import KnotService
from knot.events.event_types import CHILD_ADDED, WIDGET_CREATED

class ColumnController:
    """ Controller to handle creating a column in a table """
    app = KnotService('app')
    
    def __init__(self):
        """ Initialize the controller """
        self.headerWidget = None
        self.cellWidget = None
    
    def attachWidget(self, widget):
        """ Attach the widget """
        self.widget = widget
        widget.on(CHILD_ADDED, self.trackColumn)
        
    def trackColumn(self, widget=None, event=None):
        """ Track the Column's header """
        headers = self.widget.getChildrenWithType('header')
        if len(headers) > 0:
            self.headerWidget = headers[-1]
            
        cells = self.widget.getChildrenWithType('cell')
        if len(cells) > 0:
            self.cellWidget = cells[-1]
            
    def getData(self, scope):
        """ Return the data for the particular scope """
        content = self.cellContent
        if content is not None:
            content.scope = scope
            return content.text
        else:
            return ''
        
    @property
    def header(self):
        """ Return the header for this column """
        if self.headerWidget is None or self.headerWidget.content is None:
            return ''
        else:
            return self.headerWidget.content.text
        
    @property
    def cellContent(self):
        """ Return the header for this column """
        if self.cellWidget is None:
            return None
        else:
            return self.cellWidget.content