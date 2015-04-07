from knot.dimensions import HORIZONTAL, VERTICAL
from knot.events.event_types import RESIZED
from knot.events.tracker.parent_tracker import ParentTracker

class PercentSizing:
    """ Size a widget by taking up a percentage of the size of its parent """
    
    def __init__(self, percent, dimension):
        """ Initialize the Centerer """
        self.precent = percent
        self.dimension = dimension
        self.siblingsTracker = ParentTracker([RESIZED], self.resize)
        
    def handlesDimension(self, dimension):
        """ Return if this policy positions widgets in the given dimension """
        return dimension is self.dimension
    
    def applyToWidget(self, widget):
        """ Apply the policy to the neighbor """
        self.siblingsTracker.apply(widget)
        
    def resize(self, widget):
        """ Adjust the given widget so it is sized properly """
        width = widget.width
        height = widget.height
        
        if self.dimension is HORIZONTAL:
            width = percent*widget.parent.width
        if self.dimension is VERTICAL:
            height = percent*widget.parent.height
        
        widget.resize(width, height)