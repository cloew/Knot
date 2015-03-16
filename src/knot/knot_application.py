from .knot_window import KnotWindow
from PySide.QtGui import QApplication

import sys

class KnotApplication:
    """ Represents a Knot Application """
    
    def __init__(self):
        """ Initialize the Knot Application """
        self.app = QApplication(sys.argv)
        self.window = KnotWindow("Knot Test -- Dun Dun DUN!")
        
    def run(self):
        """ Run the applciation """
        self.app.exec_()