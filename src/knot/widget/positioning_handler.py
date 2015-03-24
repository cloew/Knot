from knot.sides import LEFT
from knot.core.positioning.from_neighbor import FromNeighbor

class PositioningHandler:
    """ Handles the positioning policy(ies) for the parent widget """
    DEFAULT_POLICY = FromNeighbor(LEFT)
    
    def __init__(self, widget, policy=None):
        """ Initialize the Handler with the widget and its positioning policy """
        self.widget = widget
        self.policy = policy
        
    def apply(self):
        """ Apply the positionig policy """
        if self.policy is None:
            self.policy = self.getDefaultPolicy()
        self.policy.applyToWidget(self.widget)
        
    def getDefaultPolicy(self):
        """ Return the default policy to be used for children """
        policy = self.getContainerDefaultPolicy()
        if policy is None:
            policy = self.DEFAULT_POLICY
        return policy
        
    def getContainerDefaultPolicy(self):
        """ Return the Container's default positioning policy """
        if self.widget.parent is not None:
            return self.widget.parent.getDefaultChildrenPolicy()
        else:
            return None
        
    def getDefaultChildrenPolicy(self):
        """ Return the default policy to be used for children """
        return self.DEFAULT_POLICY