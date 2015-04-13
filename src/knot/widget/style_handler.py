from knot.events.event_types import WIDGET_CREATED

class StyleHandler:
    """ Handle the styling for a widget """
    
    def __init__(self, widget, styling):
        """ Initialize the Handler with the tree """
        self.styling = styling
        self.widget = widget
        self.widget.on(WIDGET_CREATED, self.applyStyling)
        
    def applyStyling(self, widget=None, event=None):
        """ Apply the styling """
        self.widget._qwidget.setStyleSheet(self.styling)
        
    def setStyling(self, styling):
        """ Set the styling """
        self.styling = styling