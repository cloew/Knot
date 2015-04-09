from knot.dimensions import HORIZONTAL, VERTICAL, BOTH
from knot.directions import L2R
from knot.sides import LEFT, RIGHT, TOP, BOTTOM
from knot.policy.default_policies import DefaultPolicies
from knot.core.positioning.from_neighbor import FromNeighbor

class ContainerHandler:
    """ Handles the aspects of the widget regarding containing children """
    DEFAULT_POSITIONING = DefaultPolicies({HORIZONTAL:FromNeighbor(LEFT),
                                           VERTICAL:  FromNeighbor(TOP)})
    
    def __init__(self, widget):
        """ Initialize the Container Handler """
        self.widget = widget
        self.direction = L2R
        self.defaults = self.DEFAULT_POSITIONING
        
    def setDirection(self, direction):
        """ Set the Tree Handler's direction """
        self.direction = direction
        
    def getProperDefaults(self):
        """ Ensure the defaults are properly set up to match the direction of the children """
        self.defaults = self.DEFAULT_POSITIONING.copy(override={self.direction.dimension: FromNeighbor(self.direction.startingSide)})
        
    def getDefaultChildrenPolicies(self, dimension=BOTH):
        """ Return the default policies to be used for children """
        self.getProperDefaults()
        return self.defaults.getPolicies(dimension)
        
    def getContainerSidePosition(self, side):
        """ Return the pixel position of the given side for use for children """
        if side is LEFT:
            return 0
        elif side is RIGHT:
            return self.widget.width
        elif side is TOP:
            return 0
        elif side is BOTTOM:
            return self.widget.height