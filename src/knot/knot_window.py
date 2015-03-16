from .widget_factory import BuildWidget

from PySide.QtGui import QMainWindow

class KnotWindow(QMainWindow):
    """ Represents the window the knot elements will be rendered in """
    
    def __init__(self, title):
        """ Initialize the window """
        QMainWindow.__init__(self)
        self.setWindowTitle(title)
        self.label = BuildWidget('text', "Some Text")
        self.initUI()

    def initUI(self):
        """ Initialize the User Interface """
        self.showMaximized()
        self.label.draw(self)