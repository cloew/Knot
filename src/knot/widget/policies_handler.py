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
            self.policies = self.getDefaultPolicy(BOTH)
            if type(self.policies) is not list:
                self.policies = [self.policies]
        elif not self.policy.handlesDimension(HORIZONTAL):
            self.policies = [self.policy] + [self.getDefaultPolicy(HORIZONTAL)]
        elif not self.policy.handlesDimension(VERTICAL):
            self.policies = [self.policy] + [self.getDefaultPolicy(VERTICAL)]
        else:
            self.policies = [self.policy]
        
        for policy in self.policies:
            policy.applyToWidget(self.widget)