
class ShrinkToContents:
    """ Represents sizing a widget by making it fit its contents exactly """
    
    def adjust(self, widget):
        """ Adjust the given widget so it is sized properly """
        width = sum([child.width for child in widget.children])
        height = max([child.height for child in widget.children])
        widget.resize(width, height)