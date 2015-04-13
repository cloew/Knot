
class SetStyling:
    """ Represents a modifier to set the styling for a widget """
    
    def __init__(self, styling):
        """ Initialize with the styling string to apply """
        self.styling = styling
    
    def attachWidget(self, widget):
        """ Attach the widget """
        widget.setStyling(self.styling)