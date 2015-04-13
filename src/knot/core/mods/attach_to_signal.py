
class AttachToSignal:
    """ Represents a modifier that attaches a callback function to a signal """
    
    def __init__(self, signalName, values):
        """ Initialize with the signal name to attach to and the values to attach """
        self.signalName = signalName
        self.values = values
        
    def attachWidget(self, widget):
        """ Attach the widget """
        signal = getattr(widget.controller, self.signalName)
        for value in self.values:
            signal.register(value.get())