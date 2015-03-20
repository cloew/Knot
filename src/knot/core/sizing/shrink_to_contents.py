from knot.events.event_types import MOVED, RESIZED
from knot.events.tracker.children_tracker import ChildrenTracker

class ShrinkToContents:
    """ Represents sizing a widget by making it fit its contents exactly """
    
    def __init__(self):
        """ Initialize the Centerer """
        self.childrenTracker = ChildrenTracker([MOVED, RESIZED], self.resize)
    
    def applyToWidget(self, widget):
        """ Apply the policy to the neighbor """
        self.childrenTracker.apply(widget)
        
    def resize(self, widget):
        """ Adjust the given widget so it is sized properly """
        width = 0
        height = 0
        if len(widget.children) > 0:
            lastChild = widget.children[-1]
            width = lastChild.right
            height = lastChild.bottom
            
        widget.resize(width, height)