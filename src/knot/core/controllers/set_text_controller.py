from knot import KnotService, use_knot_services
from knot.events.event_types import WIDGET_CREATED

class SetTextController:
    """ Controller to set the text for a widget when its content changes """
    
    @use_knot_services
    def __init__(self, app=KnotService):
        """ Initialize the Set Text Controller """
        self.app = app
        
    def attachWidget(self, widget):
        """ Attach the widget """
        self.widget = widget
        widget.on(WIDGET_CREATED, self.attachChangeText)
        
    def attachChangeText(self, widget, event=None):
        """ Attach the signal to the qt signal """
        content = widget.painter.content
        content.addWatch(self.app)
        content.changed.register(self.changeText)
        
    def changeText(self, text):
        """ Update the widget's text """
        self.widget._qwidget.setText(text)
        self.widget.resizeWithPolicies()