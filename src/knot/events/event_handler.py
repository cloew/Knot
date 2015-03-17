from .event_callbacks import EventCallbacks


class EventHandler:
    """ Handles all possible widget events for a Knot Widget """
    EVENTS = {'onResize': 'resizeEvent'}
    
    def __init__(self, parent):
        """ Initialize with the widget that can fire the event """
        self.callbacks = {event:EventCallbacks(parent) for event in self.EVENTS}
        
        for event in self.callbacks:
            setattr(self, event, self.callbacks[event].addCallback)
        
    def attachEvents(self, qwidget):
        """ Attach the events to the Qt Widget """
        for key, qtMethod in self.EVENTS.items():
            callbacks = self.callbacks[key]
            setattr(qwidget, qtMethod, callbacks.fire)