from knot.dimensions import HORIZONTAL, VERTICAL, BOTH
from knot.events.event_types import DISPLAYED, RESIZED
from knot.events.tracker.widget_tracker import WidgetTracker

class UseSizeHint:
    """ Represents sizing a widget by using its size hint """
    
    def __init__(self, dimension=BOTH):
        """ Initialize the Centerer """
        self.dimension = dimension
        self.widgetTracker = WidgetTracker([DISPLAYED, RESIZED], self.resize)
    
    def applyToWidget(self, widget):
        """ Apply the policy to the neighbor """
        self.widgetTracker.apply(widget)
    
    def resize(self, widget):
        """ Adjust the given widget so it is sized properly """
        size = widget.sizeHint()
        width = widget.width
        height = widget.height
        
        if self.dimension is BOTH or self.dimension is HORIZONTAL:
            width = size.width()
        if self.dimension is BOTH or self.dimension is VERTICAL:
            height = size.height()
        
        widget.resize(width, height)