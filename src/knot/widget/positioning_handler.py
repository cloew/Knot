from knot.dimensions import HORIZONTAL, VERTICAL, BOTH
from knot.sides import LEFT, TOP
from knot.core.positioning.from_neighbor import FromNeighbor

class PositioningHandler:
    """ Handles the positioning policy(ies) for the parent widget """
    DEFAULT_POLICY = FromNeighbor(LEFT)
    DIMENSION_TO_POLICY = {HORIZONTAL:FromNeighbor(LEFT),
                           VERTICAL:  FromNeighbor(TOP)}
    
    def __init__(self, widget, policy=None):
        """ Initialize the Handler with the widget and its positioning policy """
        self.widget = widget
        self.policy = policy
        
    def apply(self):
        """ Apply the positionig policy """
        if self.policy is None:
            self.policies = self.getDefaultPolicy()
        elif not self.policy.handlesDimension(HORIZONTAL):
            self.policies = [self.policy] + self.getDefaultPolicy(HORIZONTAL)
        elif not self.policy.handlesDimension(VERTICAL):
            self.policies = [self.policy] + self.getDefaultPolicy(VERTICAL)
        else:
            self.policies = [self.policy]
        
        for policy in self.policies:
            policy.applyToWidget(self.widget)
        
    def getDefaultPolicy(self, dimension=BOTH):
        """ Return the default policy to be used for children """
        policies = self.getContainerDefaultPolicy(dimension=dimension)
        if policies is None:
            policies = self.getDefaultChildrenPolicy(dimension=dimension)
        return policies
        
    def getContainerDefaultPolicy(self, dimension=BOTH):
        """ Return the Container's default positioning policy """
        if self.widget.parent is not None:
            return self.widget.parent.getDefaultChildrenPolicy(dimension=dimension)
        else:
            return None
        
    def getDefaultChildrenPolicy(self, dimension=BOTH):
        """ Return the default policy to be used for children """
        policies = []
        if dimension is BOTH or dimension is HORIZONTAL:
            policies.append(self.DIMENSION_TO_POLICY[HORIZONTAL])
        if dimension is BOTH or dimension is VERTICAL:
            policies.append(self.DIMENSION_TO_POLICY[VERTICAL])
        return policies