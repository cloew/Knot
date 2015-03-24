from knot.dimensions import BOTH
from knot.events.event_types import DISPLAYED, RESIZED

from knot.events.tracker.parent_tracker import ParentTracker
from knot.events.tracker.widget_tracker import WidgetTracker

class Center:
    """ Modification that ensures its widget is centered in its parent """
    
    def __init__(self):
        """ Initialize the Centerer """
        self.dimension = BOTH
        self.widgetTracker = WidgetTracker([DISPLAYED, RESIZED], self.reposition)
        self.parentTracker = WidgetTracker([RESIZED], self.reposition)
        
    def handlesDimension(self, dimension):
        """ Return if this policy positions widgets in the given dimension """
        return self.dimension is BOTH or dimension is self.dimension
        
    def applyToWidget(self, widget):
        """ Apply the policy to the neighbor """
        self.widgetTracker.apply(widget)
        self.parentTracker.apply(widget)
        
    def reposition(self, widget):
        """ Reposition the widget """
        parent = widget.parent
        centerx = parent.width/2
        centery = parent.height/2
        
        widget.left = centerx - widget.width/2
        widget.top = centery - widget.height/2