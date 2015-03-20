from knot.events.event_group import EventGroup
from knot.events.event_types import CHILD_ADDED

class ChildrenTracker:
    """ Helper class to track events on a widget's children """
    
    def __init__(self, events, callback):
        """ Initialize the widget tracker """
        self.events = events
        self.callback = callback
        
    def apply(self, widget):
        """ Apply this tracker to the given widget """
        def eventCallback(aWidget, event):
            """ Callback to be used by the event that then calls the tracker's callback """
            self.callback(widget)
            
        def trackChild(parent, newChild):
            """ Track the new child """
            self.registerEvents(newChild, eventCallback)
            
        widget.on(CHILD_ADDED, trackChild)
        for child in widget.children:
            self.registerEvents(child, eventCallback)
        
    def registerEvents(self, widget, eventCallback):
        """ Return the event group """
        eventGroup = EventGroup(widget, self.events, eventCallback)
        eventGroup.register()