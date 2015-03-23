
class PositioningHandler:
    """ Handles the positioning policy(ies) for the parent widget """
    
    def __init__(self, widget, policy):
        """ Initialize the Handler with the widget and its positioning policy """
        self.widget = widget
        self.policy = policy
        
    def apply(self):
        """ Apply the positionig policy """
        self.policy.applyToWidget(self.widget)