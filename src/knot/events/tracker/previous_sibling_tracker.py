from knot.events.event_group import EventGroup

class PreviousSiblingTracker:
    """ Helper class to track events on a widget's previous sibling """
    
    def __init__(self, events, callback):
        """ Initialize the widget tracker """
        self.events = events
        self.callback = callback
        
    def apply(self, widget):
        """ Apply this tracker to the given widget """
        def eventCallback(aWidget, event):
            """ Callback to be used by the event that then calls the tracker's callback """
            self.callback(widget)
            
        previousSibling = self.findPreviousSibling(widget)
        if previousSibling is not None:
            self.registerEvents(previousSibling, eventCallback)
        
    def getEventGroup(self, widget, eventCallback):
        """ Return the event group """
        return EventGroup(self.getSubject(widget), self.events, eventCallback)
        
    def registerEvents(self, widget, eventCallback):
        """ Return the event group """
        eventGroup = EventGroup(widget, self.events, eventCallback)
        eventGroup.register()
        
    def findPreviousSibling(self, widget):
        """ Find the previous sibling of this widget """
        siblings = widget.parent.children
        currentWidgetIndex = siblings.index(widget)
        if currentWidgetIndex == 0:
            return None
        else:
            return siblings[currentWidgetIndex-1]