from knot.events.event_group import EventGroup
from knot.events.event_types import *

class Stretch:
    """ Size a widget by letting it take up as much space as needed """
    
    def applyToWidget(self, widget):
        """ Apply the policy to the neighbor """
        self.widget = widget
        
        self.siblingToResizeEventGroup = {}
        self.addResizeEvents(self.getSiblings(widget))
        self.childrenEventGroup = EventGroup(widget, [CHILD_ADDED], self.trackNewSibling)
        self.childrenEventGroup.register()
        
    def resize(self, aWidget, event):
        """ Adjust the given widget so it is sized properly """
        siblings = self.getSiblings(self.widget)
        requiredWidth = sum([sibling.width for sibling in siblings])
        
        width = self.widget.parent.width - requiredWidth
        self.widget.resize(width, self.widget.parent.height)
        
    def getSiblings(self, widget):
        """ Return the given widget's siblings """
        return [child for child in widget.parent.children if child is not widget]
        
    def addResizeEvents(self, siblings):
        """ Add Resizing Events to the siblings """
        for sibling in siblings:
            self.addSiblingResizeEvent(sibling)
            
    def addSiblingResizeEvent(self, sibling):
        """ Add resizing events to the given sibling """
        eventGroup = EventGroup(sibling, [MOVED, RESIZED], self.resize)
        self.siblingToResizeEventGroup[sibling] = eventGroup
        eventGroup.register()
            
    def trackNewSibling(self, parent, sibling=None):
        """ Track the new sibling that was added """
        self.addSiblingResizeEvent(sibling)