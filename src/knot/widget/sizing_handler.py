from .policies_handler import PoliciesHandler

from knot.dimensions import HORIZONTAL, VERTICAL, BOTH

class SizingHandler(PoliciesHandler):
    """ Handles the sizing policy(ies) for the parent widget """
        
    def getDefaultPolicy(self, dimension=BOTH):
        """ Return the default policy to be used for children """
        return self.widget.painter.DEFAULT_SIZING[dimension]