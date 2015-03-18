from .event_callbacks import EventCallbacks
from . import event_types

def GetGlobalsFrom(module):
    """ Return the Globals from a module """
    return  [getattr(module, varName) for varName in dir(module) if not varName.startswith('__')]

ALL_EVENTS = GetGlobalsFrom(event_types)

class EventHandler:
    """ Handles all possible widget events for a Knot Widget """
    QEVENTS = {event_types.MOVED: 'moveEvent',
               event_types.RESIZED: 'resizeEvent'}
    
    def __init__(self, parent):
        """ Initialize with the widget that can fire the event """
        self.callbacks = {event:EventCallbacks(parent) for event in ALL_EVENTS}
        
        # for event in self.callbacks:
            # setattr(self, event, self.callbacks[event].addCallback)
        
    def attachEvents(self, qwidget):
        """ Attach the events to the Qt Widget """
        for key, qtMethod in self.QEVENTS.items():
            callbacks = self.callbacks[key]
            setattr(qwidget, qtMethod, callbacks.fire)
            
    def on(self, eventType, callback):
        """ Add the given callback for the given event type """
        self.callbacks[eventType].addCallback(callback)
        
    def fire(self, eventType):
        """ Fire the callbacks for the given event """
        self.callbacks[eventType].fire()