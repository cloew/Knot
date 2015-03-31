from .knot_window import KnotWindow
from .service_manager import ServiceManager
from .loader.knot_loader import KnotLoader

from PySide.QtGui import QApplication

import os
import sys

class KnotApplication:
    """ Represents a Knot Application """
    
    def __init__(self, filename, root):
        """ Initialize the Knot Application """
        self.root_dir = self.getRootDirectory(root)
        self.app = QApplication(sys.argv)
        self.title = "Knot Test -- Dun Dun DUN!"
        self.window = KnotWindow()
        ServiceManager.addService('app', self)
        self.loadWidgets(filename)
        
    def getRootDirectory(self, root):
        """ Return the proper root directory """
        if not os.path.isdir(root):
            root = os.path.dirname(root)
        return root
        
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