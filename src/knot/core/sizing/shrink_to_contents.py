from knot.events.event_group import EventGroup
from knot.events.event_types import *

class ShrinkToContents:
    """ Represents sizing a widget by making it fit its contents exactly """
    
    def applyToWidget(self, widget):
        """ Apply the policy to the neighbor """
        self.widget = widget
        self.lastChild = None
        self.resizeEventGroup = None
        self.childrenEventGroup = EventGroup(widget, [CHILD_ADDED], self.findLastChild)
        self.childrenEventGroup.register()
        
        self.findLastChild(self.widget)
        
    def resize(self, lastChild, event):
        """ Adjust the given widget so it is sized properly """
        width = lastChild.right
        height = lastChild.bottom
        self.widget.resize(width, height)
            
    def findLastChild(self, widget, newChild=None):
        """ Find the last child, in case it changes """
        if len(widget.children) > 0:
            lastChild = widget.children[-1]
            
            if lastChild is not self.lastChild:
                self.lastChild = lastChild
                if self.resizeEventGroup is not None:
                    self.resizeEventGroup.unregister()
                self.resizeEventGroup = EventGroup(lastChild, [MOVED, RESIZED], self.resize)
                self.resizeEventGroup.register()
                