from knot.events.event_group import EventGroup
from knot.events.event_types import *

class FromNeighbor:
    """ Represents a positioning policy that works based on the edge of a neighbor """
    
    def __init__(self):
        """ Initialize the Form neighbor policy with the edge it should clamp to """
        
    def applyToWidget(self, widget):
        """ Apply the policy to the neighbor """
        self.widget = widget
        previousSibling = self.getPreviousSibling(widget)
        if previousSibling is not None:
            self.sibling = previousSibling
            self.widget.on(DISPLAYED, self.positionWidget)
            self.eventGroup = EventGroup(previousSibling, [MOVED, RESIZED], self.positionWidget)
            self.eventGroup.register()
    
    def positionWidget(self, aWidget, event):
        """ Position this widget relative to its sibling """
        if self.widget.canMove():
            self.widget.left = self.sibling.right
        
    def getPreviousSibling(self, widget):
        """ Return the previous sibling of this widget """
        siblings = widget.parent.children
        currentWidgetIndex = siblings.index(widget)
        if currentWidgetIndex == 0:
            return None
        else:
            return siblings[currentWidgetIndex-1]