from .knot_window import KnotWindow
from PySide.QtGui import QApplication

import sys

class KnotApplication:
    """ Represents a Knot Application """
    
    def __init__(self):
        """ Initialize the Knot Application """
        self.app = QApplication(sys.argv)
        self.title = "Knot Test -- Dun Dun DUN!"
        self.window = KnotWindow()
        
    def run(self):
        """ Run the applciation """
        self.window.draw()
        self.window.setWindowTitle(self.title)
        self.app.exec_()