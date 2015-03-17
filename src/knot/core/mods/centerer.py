
class Centerer:
    """ Modification that ensures its widget is centered in its parent """
    
    def __init__(self):
        """ Initialize the Centerer """
        
    def afterDraw(self, widget):
        """ Given the widget center it in its parent """
        parent = widget.parent
        centerx = parent.width/2
        centery = parent.height/2
        
        widget.left = centerx - widget.width/2
        widget.top = centery - widget.height/2