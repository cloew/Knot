from .policies_handler import PoliciesHandler

from knot.dimensions import HORIZONTAL, VERTICAL, BOTH
from knot.sides import LEFT, RIGHT, TOP, BOTTOM
from knot.policy.default_policies import DefaultPolicies
from knot.core.positioning.from_neighbor import FromNeighbor

class PositioningHandler(PoliciesHandler):
    """ Handles the positioning policy(ies) for the parent widget """
    DEFAULT_POSITIONING = DefaultPolicies({HORIZONTAL:FromNeighbor(LEFT),
                                           VERTICAL:  FromNeighbor(TOP)})
        
    def getDefaultPolicies(self, dimension=BOTH):
        """ Return the default policies to be used for children """
        self.getProperDefaults()
        policies = self.getContainerDefaultPolicies(dimension=dimension)
        if policies is None:
            policies = self.getDefaultChildrenPolicies(dimension=dimension)
        return policies
        
    def getProperDefaults(self):
        """ Ensure the defaults are properly set up to match the direction of the children """
        defaults = self.DEFAULT_POSITIONING.copy(override={self.widget.direction.dimension: FromNeighbor(self.widget.direction.startingSide)})
        self.DEFAULT_POSITIONING = defaults
        
    def getContainerDefaultPolicies(self, dimension=BOTH):
        """ Return the Container's default positioning policies """
        if self.widget.parent is not None:
            return self.widget.parent.getDefaultChildrenPolicies(dimension=dimension)
        else:
            return None
        
    def getDefaultChildrenPolicies(self, dimension=BOTH):
        """ Return the default policies to be used for children """
        return self.DEFAULT_POSITIONING.getPolicies(dimension)
        
    def getSidePosition(self, side):
        """ Return the pixel position of the given side """
        if side is LEFT:
            return self.widget.left
        elif side is RIGHT:
            return self.widget.right
        elif side is TOP:
            return self.widget.top
        elif side is BOTTOM:
            return self.widget.bottom
        
    def getInternalSidePosition(self, side):
        """ Return the pixel position of the given side for use for children """
        if side is LEFT:
            return 0
        elif side is RIGHT:
            return self.widget.width
        elif side is TOP:
            return 0
        elif side is BOTTOM:
            return self.widget.height
        
    def setSidePosition(self, side, value):
        """ Set the pixel position of the given side """
        if side is LEFT:
            self.widget.left = value
        elif side is RIGHT:
            self.widget.right = value
        elif side is TOP:
            self.widget.top = value
        elif side is BOTTOM:
            self.widget.bottom = value