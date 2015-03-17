
class LeftToRight:
    """ Method of positioning a widget based on the previous widget's right end """
    
    def position(self, widget, previous):
        """ Position the widget from the right end of the previous widget """
        if previous is not None:
            widget.left = previous.right