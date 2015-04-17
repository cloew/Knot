from knot.dimensions import BOTH, HORIZONTAL, VERTICAL
from knot.events.event_types import DISPLAYED, RESIZED

from knot.events.tracker.parent_tracker import ParentTracker
from knot.events.tracker.widget_tracker import WidgetTracker

class Center:
    """ Modification that ensures its widget is centered in its parent """
    
    def __init__(self, dimension=BOTH):
        """ Initialize the Centerer """
        self.dimension = dimension
        self.widgetTracker = WidgetTracker([DISPLAYED, RESIZED], self.reposition)
        self.parentTracker = ParentTracker([RESIZED], self.reposition)
        
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
        
        newLeft = widget.left
        newTop = widget.top
        
        if self.dimension is BOTH or self.dimension is HORIZONTAL:
            newLeft = centerx - widget.width/2
        
        if self.dimension is BOTH or self.dimension is VERTICAL:
            newTop = centery - widget.height/2
            
        widget.left = newLeft
        widget.top = newTop