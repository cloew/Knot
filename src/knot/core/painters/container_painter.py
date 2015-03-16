
class ContainerPainter:
    """ Handles painting a collection of child widgets """
    
    def __init__(self, content):
        """ Initialize the Painter with its content """
        pass
    
    def drawChildren(self, widget, qwidget):
        """ Draws the children widgets """
        previous = None
        for child in widget.children:
            self.drawChild(child, qwidget)
            self.positionChild(child, previous)
            previous = child
            
    def drawChild(self, child, qwidget):
        """ Draw the child """
        child.draw()
        child._qwidget.setParent(qwidget)
        child.show()
            
    def positionChild(self, child, previous):
        """ Give the child widget the proper position """