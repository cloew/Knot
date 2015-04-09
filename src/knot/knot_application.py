from .knot_window import KnotWindow
from .service_manager import ServiceManager
from .watch_manager import WatchManager
from .loader.knot_loader import KnotLoader

from kao_resources import ResourceDirectory
from PySide.QtGui import QApplication

import sys

class KnotApplication:
    """ Represents a Knot Application """
    
    def __init__(self, config):
        """ Initialize the Knot Application """
        self.app = QApplication(sys.argv)
        self.resourceDirectory = config.rootDirectory
        
        ServiceManager.addService('app', self)
        self.watchManager = WatchManager()
        
        self.window = KnotWindow(title=config.title)
        self.loadWidgets(config.knotFilename)
        
    def loadWidgets(self, filename):
        """ Load the widgets onto the window """
        loader = KnotLoader(filename)
        loader.loadOnto(self.window)
        
    def run(self):
        """ Run the application """
        self.watchManager.start()
        self.window.draw()
        self.app.exec_()
        
    def watch(self, obj, varName, callback):
        """ Watch the given variable for changes """
        self.watchManager.addWatch(obj, varName, callback)