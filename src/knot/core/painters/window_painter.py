from PySide.QtGui import QMainWindow
from .left_to_right_painter import LeftToRightPainter

class WindowPainter(LeftToRightPainter):
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