from .widget import Widget
from knot.core.painters.text_painter import TextPainter

from PySide.QtGui import QApplication, QLabel, QMainWindow

class KnotWindow(QMainWindow):
    """ Represents the window the knot elements will be rendered in """
    
    def __init__(self, title):
        """ Initialize the window """
        QMainWindow.__init__(self)
        self.setWindowTitle(title)
        self.label = Widget(TextPainter("Some Text"))
        self.initUI()

    def initUI(self):
        """ Initialize the User Interface """
        self.showMaximized()
        self.label.draw(self)