from .left_to_right_painter import LeftToRightPainter

from PySide.QtGui import QMainWindow

class WindowPainter(LeftToRightPainter):
    """ Handles creation of the Qt widget to represent the window """
        
    def draw(self, widget):
        """ Draw the Text Painter """
        qwidget = QMainWindow()
        qwidget.showMaximized()
        
        self.drawChildren(widget, qwidget)
        
        return qwidget