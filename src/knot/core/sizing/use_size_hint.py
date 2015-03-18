from knot.events.event_types import *

class UseSizeHint:
    """ Represents sizing a widget by using its size hint """
    
    def applyToWidget(self, widget):
        """ Apply the policy to the neighbor """
        widget.on(MOVE, self.resize)
    
    def resize(self, widget, event):
        """ Adjust the given widget so it is sized properly """
        widget.resize(widget.sizeHint())