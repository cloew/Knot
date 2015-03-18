
class EventCallbacks:
    """ Collection of callbacks for a Widget Event """
    
    def __init__(self, parent):
        """ Initialize with the widget that can fire the event """
        self.parent = parent
        self.callbacks = []
        
    def addCallback(self, callback):
        """ Add the given callback to the list of events to fire """
        self.callbacks.append(callback)
        
    def fire(self, event=None):
        """ Fires this event """
        [callback(self.parent, event) for callback in self.callbacks]