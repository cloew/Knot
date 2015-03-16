from PySide.QtGui import QMainWindow

class WindowPainter:
    """ Handles creation of the Qt widget to represent the window """
    
    def __init__(self, content):
        """ Initialize the Painter with its internal content """
        pass
        
    def draw(self):
        """ Draw the Text Painter """
        widget = QMainWindow()
        widget.showMaximized()
        return widget