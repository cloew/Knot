from knot.dimensions import BOTH

class SizingDefaultsProvider:
    """ Handles providing the default sizing policy(ies) """
    
    def __init__(self, widget):
        """ Initialize with the current widget """
        self.widget = widget
        
    def getDefaultPolicies(self, dimension=BOTH):
        """ Return the default policies to be used for children """
        return self.widget.painter.DEFAULT_SIZING.getPolicies(dimension)
        
    def resizeWithPolicies(self):
        """ Resize the widget """
        [policy.resize(self.widget) for policy in self.policies]