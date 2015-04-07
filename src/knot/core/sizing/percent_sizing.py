from knot.dimensions import HORIZONTAL, VERTICAL
from knot.events.event_types import DISPLAYED, RESIZED
from knot.events.tracker.parent_tracker import ParentTracker
from knot.events.tracker.widget_tracker import WidgetTracker

class PercentSizing:
    """ Size a widget by taking up a percentage of the size of its parent """
    
    def __init__(self, percent, dimension):
        """ Initialize the Centerer """
        self.percent = percent
        self.dimension = dimension
        self.widgetTracker = WidgetTracker([DISPLAYED], self.resize)
        self.parentTracker = ParentTracker([RESIZED], self.resize)
        
    def handlesDimension(self, dimension):
        """ Return if this policy positions widgets in the given dimension """
        return dimension is self.dimension
    
    def applyToWidget(self, widget):
        """ Apply the policy to the neighbor """
        self.widgetTracker.apply(widget)
        self.parentTracker.apply(widget)
        
    def resize(self, widget):
        """ Adjust the given widget so it is sized properly """
        width = widget.width
        height = widget.height
        if self.dimension is HORIZONTAL:
            width = self.percent*widget.parent.width
        if self.dimension is VERTICAL:
            height = self.percent*widget.parent.height
        
        widget.resize(width, height)