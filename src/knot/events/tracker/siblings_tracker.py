from knot.events.event_group import EventGroup
from knot.events.event_types import CHILD_ADDED, DISPLAYED, HIDDEN

class SiblingsTracker:
    """ Helper class to track events on a widget's siblings """
    
    def __init__(self, events, callback):
        """ Initialize the widget tracker """
        self.events = events + [DISPLAYED, HIDDEN]
        self.callback = callback
        
    def apply(self, widget):
        """ Apply this tracker to the given widget """
        def eventCallback(aWidget, event):
            """ Callback to be used by the event that then calls the tracker's callback """
            self.callback(widget)
            
        def trackSibling(parent, newSibling):
            """ Track the new child """
            self.registerEvents(newSibling, eventCallback)
            
        widget.parent.on(CHILD_ADDED, trackSibling)
        for child in widget.siblings:
            self.registerEvents(child, eventCallback)
        
    def registerEvents(self, widget, eventCallback):
        """ Return the event group """
        eventGroup = EventGroup(widget, self.events, eventCallback)
        eventGroup.register()