from knot import KnotService
from knot.events.event_types import CHILD_ADDED, WIDGET_CREATED

class ColumnController:
    """ Controller to handle creating a column in a table """
    app = KnotService('app')
    
    def __init__(self):
        """ Initialize the controller """
        self.headerWidget = None
    
    def attachWidget(self, widget):
        """ Attach the widget """
        self.widget = widget
        widget.on(CHILD_ADDED, self.trackColumn)
        
    def trackColumn(self, widget=None, event=None):
        """ Track the Column's header """
        headers = self.widget.getChildrenWithType('header')
        if len(headers) > 0:
            self.headerWidget = headers[-1]
        
    @property
    def header(self):
        """ Return the header for this column """
        if self.headerWidget is None or self.headerWidget.content is None:
            return ''
        else:
            return self.headerWidget.content.text