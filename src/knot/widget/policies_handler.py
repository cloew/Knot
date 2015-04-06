from knot.dimensions import HORIZONTAL, VERTICAL, BOTH

class PoliciesHandler:
    """ Handles the policies for the parent widget """
    
    def __init__(self, widget, policy=None):
        """ Initialize the Handler with the widget and its positioning policy """
        self.widget = widget
        self.policy = policy
        
    def apply(self, widget=None, event=None):
        """ Apply the positionig policy """
        if self.policy is None:
            self.policies = self.getDefaultPolicies(BOTH)
        elif not self.policy.handlesDimension(HORIZONTAL):
            self.policies = [self.policy] + self.getDefaultPolicies(HORIZONTAL)
        elif not self.policy.handlesDimension(VERTICAL):
            self.policies = [self.policy] + self.getDefaultPolicies(VERTICAL)
        else:
            self.policies = [self.policy]
        
        for policy in self.policies:
            policy.applyToWidget(self.widget)