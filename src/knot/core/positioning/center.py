from knot.events.event_group import EventGroup
from knot.events.event_types import *

class Center:
    """ Modification that ensures its widget is centered in its parent """
    
    def __init__(self):
        """ Initialize the Centerer """
        
    def applyToWidget(self, widget):
        """ Apply the policy to the neighbor """
        self.widget = widget
        self.widget.on(DISPLAYED, self.positionWidget)
        self.widget.parent.on(RESIZED, self.positionWidget)
    
    def positionWidget(self, aWidget, event):
        """ Center the widget in its parent """
        parent = self.widget.parent
        centerx = parent.width/2
        centery = parent.height/2
        
        self.widget.left = centerx - self.widget.width/2
        self.widget.top = centery - self.widget.height/2