from PySide.QtGui import QWidget

class LeftToRightPainter:
    """ Handles creation of a Qt widget for wrapping chidlren widgets that are placed horizontally """
    
    def __init__(self, content):
        """ Initialize the Painter with its content """
        pass
        
    def draw(self, widget):
        """ Draw the Text Painter """
        qwidget = QWidget()
        self.drawChildren(widget, qwidget)
        self.shrinkContainer(widget, qwidget)
        return qwidget
        
    def shrinkContainer(self, widget, qwidget):
        """ Shrink the container widget so it exactly fits its contents """
        width = sum([child.width for child in widget.children])
        height = max([child.height for child in widget.children])
        qwidget.resize(width, height)
        
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
        """ Draw the child """
        if previous is not None:
            child.left = previous.right