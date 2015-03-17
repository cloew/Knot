from .container_painter import ContainerPainter
from .left_to_right_painter import LeftToRightPainter

from PySide.QtGui import QMainWindow

class WindowPainter(LeftToRightPainter):
    """ Handles creation of the Qt widget to represent the window """
    
    def __init__(self, content):
        """ Initialize the painter """
        LeftToRightPainter.__init__(self, content, sizing=None)
        
    def buildQWidget(self, widget):
        """ Draw the Main Window and tell it to maximize """
        qwidget = QMainWindow()
        qwidget.showMaximized()
        return qwidget
        
    # def afterDrawWidget(self, widget, qwidget):
        # """ Use the Container Painter's after draw then shrink this widget so it fits its children exactly """
        # ContainerPainter.afterDrawWidget(self, widget, qwidget)