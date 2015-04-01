from knot.dimensions import HORIZONTAL, VERTICAL, BOTH

class PoliciesHandler:
    """ Handles the policies for the parent widget """
    
    def __init__(self, widget, policy=None):
        """ Initialize the Handler with the widget and its positioning policy """
        self.widget = widget
        self.policy = policy
        
    def apply(self):
        """ Apply the positionig policy """
        if self.policy is None:
            self.policies = self.getDefaultPolicyAsList(BOTH)
        elif not self.policy.handlesDimension(HORIZONTAL):
            self.policies = [self.policy] + self.getDefaultPolicyAsList(HORIZONTAL)
        elif not self.policy.handlesDimension(VERTICAL):
            self.policies = [self.policy] + self.getDefaultPolicyAsList(VERTICAL)
        else:
            self.policies = [self.policy]
        
        for policy in self.policies:
            policy.applyToWidget(self.widget)
            
    def getDefaultPolicyAsList(self, dimension):
        """ Return the requested default policies as a list if necessary """
        policies = self.getDefaultPolicy(dimension)
        if type(policies) is not list:
            policies = [policies]
        return policies