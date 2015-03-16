
class Widget:
    """ Represents a widget within Knot """
    
    def __init__(self, painter):
        """ Initialize the widget with its painters """
        self.painter = painter
        
    def draw(self, parent):
        """ Draw the widget given its parent """
        widget = self.painter.draw()
        widget.setParent(parent)
        widget.show()