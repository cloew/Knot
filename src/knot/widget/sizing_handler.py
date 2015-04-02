from .policies_handler import PoliciesHandler

from knot.dimensions import HORIZONTAL, VERTICAL, BOTH

class SizingHandler(PoliciesHandler):
    """ Handles the sizing policy(ies) for the parent widget """
        
    def getDefaultPolicies(self, dimension=BOTH):
        """ Return the default policies to be used for children """
        return self.widget.painter.DEFAULT_SIZING.getPolicies(dimension)