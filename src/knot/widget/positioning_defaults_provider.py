from knot.dimensions import HORIZONTAL, VERTICAL, BOTH
from knot.sides import LEFT, TOP
from knot.policy.default_policies import DefaultPolicies
from knot.core.positioning.from_neighbor import FromNeighbor

class PositioningDefaultsProvider:
    """ Handles providing the default positioning policy(ies) """
    DEFAULT_POSITIONING = DefaultPolicies({HORIZONTAL:FromNeighbor(LEFT),
                                           VERTICAL:  FromNeighbor(TOP)})
                                           
    def __init__(self, widget):
        """ Initialize with the current widget """
        self.widget = widget
        
    def getDefaultPolicies(self, dimension=BOTH):
        """ Return the default policies to be used for children """
        policies = self.getContainerDefaultPolicies(dimension=dimension)
        if policies is None:
            policies = self.widget.getDefaultChildrenPolicies(dimension=dimension)
        return policies
        
    def getProperDefaults(self):
        """ Ensure the defaults are properly set up to match the direction of the children """
        self.defaults = self.DEFAULT_POSITIONING.copy(override={self.widget.direction.dimension: FromNeighbor(self.widget.direction.startingSide)})
        
    def getContainerDefaultPolicies(self, dimension=BOTH):
        """ Return the Container's default positioning policies """
        if self.widget.parent is not None:
            return self.widget.parent.getDefaultChildrenPolicies(dimension=dimension)
        else:
            return None