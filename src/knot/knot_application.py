from .knot_window import KnotWindow
from .loader.knot_loader import KnotLoader
from PySide.QtGui import QApplication

import sys

class KnotApplication:
    """ Represents a Knot Application """
    
    def __init__(self, filename):
        """ Initialize the Knot Application """
        self.app = QApplication(sys.argv)
        self.title = "Knot Test -- Dun Dun DUN!"
        self.window = KnotWindow()
        self.loadWidgets(filename)
        
    def loadWidgets(self, filename):
        """ Load the widgets onto the window """
        loader = KnotLoader(filename)
        widgets = loader.load()
        for widget in widgets:
            self.window.addChild(widget)
        
    def run(self):
        """ Run the applciation """
        self.window.draw()
        self.window.setWindowTitle(self.title)
        self.app.exec_()