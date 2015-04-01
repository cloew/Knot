from .knot_window import KnotWindow
from .service_manager import ServiceManager
from .loader.knot_loader import KnotLoader

from kao_resources import ResourceDirectory
from PySide.QtGui import QApplication

import sys

class KnotApplication:
    """ Represents a Knot Application """
    
    def __init__(self, filename, root):
        """ Initialize the Knot Application """
        self.resourceDirectory = ResourceDirectory(root)
        self.app = QApplication(sys.argv)
        self.window = KnotWindow(title="Knot Test -- Dun Dun DUN!")
        ServiceManager.addService('app', self)
        self.loadWidgets(filename)
        
    def loadWidgets(self, filename):
        """ Load the widgets onto the window """
        loader = KnotLoader(filename)
        loader.loadOnto(self.window)
        
    def run(self):
        """ Run the applciation """
        self.window.draw()
        self.app.exec_()