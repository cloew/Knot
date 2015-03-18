from knot.events.event_types import *

class FromNeighbor:
    """ Represents a positioning policy that works based on the edge of a neighbor """
    
    def __init__(self):
        """ Initialize the Form neighbor policy with the edge it should clamp to """
        
    def applyToWidget(self, widget):
        """ Apply the policy to the neighbor """
        previousSibling = self.getPreviousSibling(widget)
        if previousSibling is not None:
            callback = self.getCallback(widget)
            
            previousSibling.on(MOVED, callback)
            previousSibling.on(RESIZED, callback)
        
    def getCallback(self, widget):
        """ Return the callback to position the given widget """
        def positionWidget(sibling, event):
            """ Position this widget relative to its sibling """
            widget.left = sibling.right
        return positionWidget
        
    def getPreviousSibling(self, widget):
        """ Return the previous sibling of this widget """
        siblings = widget.parent.children
        currentWidgetIndex = siblings.index(widget)
        if currentWidgetIndex == 0:
            return None
        else:
            return siblings[currentWidgetIndex-1]