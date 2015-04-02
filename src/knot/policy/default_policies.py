from knot.dimensions import HORIZONTAL, VERTICAL, BOTH

class DefaultPolicies:
    """ Represents the default policies based on a requested dimension """
    
    def __init__(self, dimensionToPolicy):
        """ Initialize the Defaults with the dimensiojn ot the corresponding policy(ies) """
        self.dimensionToPolicy = dimensionToPolicy
        
        if BOTH not in self.dimensionToPolicy:
            self.dimensionToPolicy[BOTH] = [self.dimensionToPolicy[HORIZONTAL], self.dimensionToPolicy[VERTICAL]]
            
        self.convertPolicyToList(HORIZONTAL)
        self.convertPolicyToList(VERTICAL)
            
    def getPolicies(self, dimension):
        """ Return the policies for the given dimension """
        return self.dimensionToPolicy[dimension]
        
    def convertPolicyToList(self, dimension):
        """ Convert the policy for the given Dimension to a list """
        self.dimensionToPolicy[dimension] = [self.dimensionToPolicy[dimension]]