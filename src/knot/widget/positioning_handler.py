from .policies_handler import PoliciesHandler

from knot.dimensions import HORIZONTAL, VERTICAL, BOTH
from knot.sides import LEFT, TOP
from knot.core.positioning.from_neighbor import FromNeighbor

class PositioningHandler(PoliciesHandler):
    """ Handles the positioning policy(ies) for the parent widget """
    DEFAULT_POLICY = FromNeighbor(LEFT)
    DIMENSION_TO_POLICY = {HORIZONTAL:FromNeighbor(LEFT),
                           VERTICAL:  FromNeighbor(TOP)}
        
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