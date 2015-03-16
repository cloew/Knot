from knot.core.painters.text_painter import TextPainter

from PySide.QtGui import QApplication, QLabel, QMainWindow

class KnotWindow(QMainWindow):
    """ Represents the window the knot elements will be rendered in """
    
    def __init__(self, title):
        """ Initialize the window """
        QMainWindow.__init__(self)
        self.setWindowTitle(title)
        self.textPainter = TextPainter("Some Text")
        self.initUI()

    def initUI(self):
        """ Initialize the User Interface """
        self.statusBar()
        self.showMaximized()
        
        widget = self.textPainter.draw()
        widget.setParent(self)
        print(widget.geometry())
        print(self.pos())
        print(widget.pos())
        widget.show()