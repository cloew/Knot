from knot.dimensions import HORIZONTAL, VERTICAL, BOTH
from knot.events.event_types import MOVED, RESIZED
from knot.events.tracker.siblings_tracker import SiblingsTracker

class Stretch:
    """ Size a widget by letting it take up as much space as needed """
    
    def __init__(self, dimension=BOTH):
        """ Initialize the Centerer """
        self.dimension = dimension
        self.siblingsTracker = SiblingsTracker([MOVED, RESIZED], self.resize)
        
    def handlesDimension(self, dimension):
        """ Return if this policy positions widgets in the given dimension """
        return self.dimension is BOTH or dimension is self.dimension
    
    def applyToWidget(self, widget):
        """ Apply the policy to the neighbor """
        self.siblingsTracker.apply(widget)
        
    def resize(self, widget):
        """ Adjust the given widget so it is sized properly """
        width = widget.width
        height = widget.height
        
        if self.dimension is BOTH or self.dimension is HORIZONTAL:
            siblings = widget.siblings
            requiredWidth = sum([sibling.width for sibling in siblings])
            width = widget.parent.width - requiredWidth
        if self.dimension is BOTH or self.dimension is VERTICAL:
            height = widget.parent.height
        
        widget.resize(width, height)