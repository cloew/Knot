
class EventGroup:
    """ Represents a group of events that should be applied """
    
    def __init__(self, widget, events, callback):
        """ Build the vent group with the widget, events to attach to and the callback to run """
        self.widget = widget
        self.events = events
        self.callback = callback
        
    def register(self):
        """ Register this Event Group """
        for event in self.events:
            self.widget.on(event, self.callback)
        
    def unregister(self):
        """ Unregister this Event Group """
        for event in self.events:
            self.widget.unregister(event, self.callback)