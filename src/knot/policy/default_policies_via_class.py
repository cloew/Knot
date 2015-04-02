from knot.dimensions import HORIZONTAL, VERTICAL, BOTH

class DefaultPoliciesViaClass:
    """ Represents the default policies using a class that accepts the dimension """
    
    def __init__(self, policyClass):
        """ Initialize the default policies with the policy class """
        self.dimensionToPolicy = {}
        
        for dimension in [HORIZONTAL, VERTICAL, BOTH]:
            self.dimensionToPolicy[dimension] = [policyClass(dimension=dimension)]
            
    def getPolicies(self, dimension):
        """ Return the policies for the given dimension """
        return self.dimensionToPolicy[dimension]