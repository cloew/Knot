from knot.events.event_group import EventGroup
from knot.events.event_types import DISPLAYED, RESIZED
from knot.events.tracker.widget_tracker import WidgetTracker

class Center:
    """ Modification that ensures its widget is centered in its parent """
    
    def __init__(self):
        """ Initialize the Centerer """
        self.widgetTracker = WidgetTracker([DISPLAYED, RESIZED], self.reposition)
        
    def applyToWidget(self, widget):
        """ Apply the policy to the neighbor """
        self.widget = widget
        self.widgetTracker.apply(widget)
        self.widget.parent.on(RESIZED, self.positionWidget)
    
    def positionWidget(self, aWidget, event):
        """ Center the widget in its parent """
        self.reposition(self.widget)
        
    def reposition(self, widget):
        """ Reposition the widget """
        parent = widget.parent
        centerx = parent.width/2
        centery = parent.height/2
        
        widget.left = centerx - widget.width/2
        widget.top = centery - widget.height/2