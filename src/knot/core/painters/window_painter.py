from PySide.QtGui import QMainWindow

class WindowPainter:
    """ Handles creation of the Qt widget to represent the window """
    
    def __init__(self, content):
        """ Initialize the Painter with its internal content """
        pass
        
    def draw(self, widget):
        """ Draw the Text Painter """
        qwidget = QMainWindow()
        qwidget.showMaximized()
        
        self.drawChildren(widget, qwidget)
        
        return qwidget
        
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