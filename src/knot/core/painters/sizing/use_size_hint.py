
class UseSizeHint:
    """ Represents sizing a widget by using its size hint """
    
    def adjust(self, widget):
        """ Adjust the given widget so it is sized properly """
        widget.resize(widget.sizeHint())