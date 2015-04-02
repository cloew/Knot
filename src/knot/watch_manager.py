from .watches.var_watch import VarWatch

from PySide.QtCore import QTimer

class WatchManager:
    """ Helper class to manage the active watches for a knot application """
    WATCH_REFRESH_DELAY = 10
    
    def __init__(self):
        """ Initialize the Watch Manager """
        self.watches = []
        self.timer = QTimer()
        self.timer.setInterval(self.WATCH_REFRESH_DELAY)
        self.timer.timeout.connect(self.checkWatches)
        
    def start(self):
        """ Start the Watch Manager """
        self.timer.start()
        
    def addWatch(self, obj, varName, callback):
        """ Add the given watch """
        self.watches.append(VarWatch(obj, varName, callback))
        
    def checkWatches(self):
        """ Check the watches """
        for watch in self.watches:
            watch.checkChange()