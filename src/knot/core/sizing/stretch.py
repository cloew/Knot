from knot.events.event_group import EventGroup
from knot.events.event_types import *
from knot.events.tracker.siblings_tracker import SiblingsTracker

class Stretch:
    """ Size a widget by letting it take up as much space as needed """
    
    def __init__(self):
        """ Initialize the Centerer """
        self.siblingsTracker = SiblingsTracker([MOVED, RESIZED], self.resize)
    
    def applyToWidget(self, widget):
        """ Apply the policy to the neighbor """
        self.siblingsTracker.apply(widget)
        
    def resize(self, widget):
        """ Adjust the given widget so it is sized properly """
        siblings = widget.siblings
        requiredWidth = sum([sibling.width for sibling in siblings])
        
        width = widget.parent.width - requiredWidth
        widget.resize(width, widget.parent.height)