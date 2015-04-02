
class Signal:
    """ Represents a signal that a controller can emit to call callback methods """
    
    def __init__(self):
        """ Initialize the signal """
        self.callbacks = []
        
    def emit(self, *args, **kwargs):
        """ Emit the signal and call all the registered callbacks """
        for callback in self.callbacks:
            callback(*args, **kwargs)
            
    def register(self, callback):
        """ Register the given callback """
        self.callbacks.append(callback)