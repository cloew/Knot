from knot.events.event_group import EventGroup

class WidgetTracker:
    """ Helper class to track specific events on a widget and fire a callback """
    
    def __init__(self, events, callback):
        """ Initialize the widget tracker """
        self.events = events
        self.callback = callback
        
    def apply(self, widget):
        """ Apply this tracker to the given widget """
        def eventCallback(aWidget, event):
            """ Callback to be used by the event that then calls the tracker's callback """
            self.callback(widget)
        eventGroup = self.getEventGroup(widget, eventCallback)
        eventGroup.register()
        
    def getEventGroup(self, widget, eventCallback):
        """ Return the event group """
        return EventGroup(widget, self.events, eventCallback)