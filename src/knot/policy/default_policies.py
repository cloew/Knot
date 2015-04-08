from knot.dimensions import HORIZONTAL, VERTICAL, BOTH

class DefaultPolicies:
    """ Represents the default policies based on a requested dimension """
    
    def __init__(self, dimensionToPolicy):
        """ Initialize the Defaults with the dimensiojn ot the corresponding policy(ies) """
        self._dimensionToPolicy = dimensionToPolicy
        self.dimensionToPolicy = dimensionToPolicy
        
        if BOTH not in self.dimensionToPolicy:
            self.dimensionToPolicy[BOTH] = [self._dimensionToPolicy[HORIZONTAL], self._dimensionToPolicy[VERTICAL]]
            
        for dimension in [HORIZONTAL, VERTICAL]:
            self.dimensionToPolicy[dimension] = self.convertPolicyToList(dimension)
            
    def getPolicies(self, dimension):
        """ Return the policies for the given dimension """
        return self.dimensionToPolicy[dimension]
        
    def convertPolicyToList(self, dimension):
        """ Convert the policy for the given Dimension to a list """
        value = []
        if dimension in self._dimensionToPolicy:
            value = [self._dimensionToPolicy[dimension]]
        return value
                
    def copy(self, override={}):
        """ Copy the Default Policies while optionally overriding the defaults """
        newDefaults = dict(self._dimensionToPolicy)
        newDefaults.update(override)
        return DefaultPolicies(newDefaults)