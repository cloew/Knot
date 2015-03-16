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
        for child in widget.children:
            child.draw(widget)
            child._qwidget.setParent(qwidget)
            child.show()