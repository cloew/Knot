
class ContainerPainter:
    """ Handles painting a collection of child widgets """
    
    def __init__(self, positioner):
        """ Initialize the Container Painter with its method for positioning child widgets """
        self.positioner = positioner
    
    def drawChildren(self, widget, qwidget):
        """ Draws the children widgets """
        previous = None
        for child in widget.children:
            self.drawChild(child, qwidget)
            self.positioner.position(child, previous)
            previous = child
            
    def drawChild(self, child, qwidget):
        """ Draw the child """
        child.draw()
        child._qwidget.setParent(qwidget)
        child.show()