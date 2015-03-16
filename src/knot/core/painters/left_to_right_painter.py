from .container_painter import ContainerPainter

from PySide.QtGui import QWidget

class LeftToRightPainter(ContainerPainter):
    """ Handles creation of a Qt widget for wrapping chidlren widgets that are placed horizontally """
        
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
            
    def positionChild(self, child, previous):
        """ Draw the child """
        if previous is not None:
            child.left = previous.right