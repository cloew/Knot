
class SizingHandler:
    """ Handles the sizing policy(ies) for the parent widget """
    
    def __init__(self, widget, policy):
        """ Initialize the Handler with the widget and its sizing policy """
        self.widget = widget
        if policy is None:
            policy = widget.painter.DEFAULT_SIZING
        self.policy = policy
        
    def apply(self):
        """ Apply the positionig policy """
        if self.policy is not None:
            self.policy.applyToWidget(self.widget)