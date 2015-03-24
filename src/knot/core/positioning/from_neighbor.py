from knot.sides import LEFT

from knot.events.event_types import DISPLAYED, MOVED, RESIZED
from knot.events.tracker.previous_sibling_tracker import PreviousSiblingTracker
from knot.events.tracker.widget_tracker import WidgetTracker

class FromNeighbor:
    """ Represents a positioning policy that works based on the edge of a neighbor """
    
    def __init__(self, side):
        """ Initialize the Form neighbor policy with the edge it should clamp to """
        self.side = side
        self.widgetTracker = WidgetTracker([DISPLAYED], self.reposition)
        self.prevSiblingTracker = PreviousSiblingTracker([MOVED, RESIZED], self.reposition)
        
    def applyToWidget(self, widget):
        """ Apply the policy to the neighbor """
        self.widgetTracker.apply(widget)
        self.prevSiblingTracker.apply(widget)
    
    def reposition(self, widget):
        """ Position this widget relative to its sibling """
        if self.side is LEFT:
            sibling = self.getPreviousSibling(widget)
            if sibling is not None and widget.canMove():
                widget.left = sibling.right
        
    def getPreviousSibling(self, widget):
        """ Return the previous sibling of this widget """
        siblings = widget.parent.children
        currentWidgetIndex = siblings.index(widget)
        if currentWidgetIndex == 0:
            return None
        else:
            return siblings[currentWidgetIndex-1]