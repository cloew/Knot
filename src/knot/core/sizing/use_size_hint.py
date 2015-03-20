from knot.events.event_types import DISPLAYED, RESIZED
from knot.events.tracker.widget_tracker import WidgetTracker

class UseSizeHint:
    """ Represents sizing a widget by using its size hint """
    
    def __init__(self):
        """ Initialize the Centerer """
        self.widgetTracker = WidgetTracker([DISPLAYED, RESIZED], self.resize)
    
    def applyToWidget(self, widget):
        """ Apply the policy to the neighbor """
        self.widgetTracker.apply(widget)
    
    def resize(self, widget):
        """ Adjust the given widget so it is sized properly """
        widget.resize(widget.sizeHint())