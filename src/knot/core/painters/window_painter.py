from .container_painter import ContainerPainter

from PySide.QtGui import QMainWindow

class WindowPainter(ContainerPainter):
    """ Handles creation of the Qt widget to represent the window """
    
    def __init__(self, content):
        """ Initialize the painter """
        ContainerPainter.__init__(self, content, sizing=None)
        
    def buildQWidget(self, widget):
        """ Draw the Main Window and tell it to maximize """
        qwidget = QMainWindow()
        qwidget.showMaximized()
        return qwidget