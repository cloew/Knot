from knot.sides import LEFT

from knot.events.event_types import DISPLAYED, MOVED, RESIZED
from knot.events.tracker.previous_sibling_tracker import PreviousSiblingTracker
from knot.events.tracker.parent_tracker import ParentTracker
from knot.events.tracker.siblings_tracker import SiblingsTracker
from knot.events.tracker.widget_tracker import WidgetTracker

class FromNeighbor:
    """ Represents a positioning policy that works based on the edge of a neighbor """
    
    def __init__(self, side):
        """ Initialize the Form neighbor policy with the edge it should clamp to """
        self.side = side
        self.parentTracker = ParentTracker([RESIZED], self.reposition)
        self.siblingsTracker = SiblingsTracker([MOVED, RESIZED], self.reposition)
        self.widgetTracker = WidgetTracker([DISPLAYED], self.reposition)
        
    def handlesDimension(self, dimension):
        """ Return if this policy positions widgets in the given dimension """
        return dimension is self.side.dimension
        
    def applyToWidget(self, widget):
        """ Apply the policy to the neighbor """
        self.parentTracker.apply(widget)
        self.siblingsTracker.apply(widget)
        self.widgetTracker.apply(widget)
    
    def reposition(self, widget):
        """ Position this widget relative to its sibling """
        if widget.canMove():
            sibling = widget.getSiblingOn(self.side)
            edgePosition = None
            if sibling is not None:
                edgePosition = sibling.getSidePosition(self.side.oppositeSide)
            else:
                edgePosition = widget.parent.getInternalSidePosition(self.side)
            widget.setSidePosition(self.side, edgePosition)
            
    def __repr__(self):
        """ Return the String representation of this object """
        return "<FromNeighbor({0})>".format(self.side)