from knot import KnotService
from knot.events.event_types import CHILD_ADDED, WIDGET_CREATED

class TabController:
    """ Controller to handle loading the label for a tab """
    app = KnotService('app')
    
    def __init__(self):
        """ Initialize the controller """
        self.labelWidegt = None
    
    def attachWidget(self, widget):
        """ Attach the widget """
        self.widget = widget
        widget.on(CHILD_ADDED, self.trackLabel)
        
    def trackLabel(self, widget=None, event=None):
        """ Track the Tab's label """
        labels = self.widget.getChildrenWithType('label')
        if len(labels) > 0:
            self.labelWidget = labels[-1]
        
    @property
    def label(self):
        """ Return the label for this tab """
        if self.labelWidget is None or self.labelWidget.content is None:
            return ''
        else:
            return self.labelWidget.content.text