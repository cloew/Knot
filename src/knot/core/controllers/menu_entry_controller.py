from knot.events.event_types import PARENT_ADDED
from knot.events.signal import Signal

class MenuEntryController:
    """ Handles the attachment of an entry to a Context Menu """
    
    def __init__(self):
        """ Initialize the Menu Entry """
        self.action = None
        self.triggered = Signal()
        
    def attachWidget(self, widget):
        """ Attach to the widget """
        self.widget = widget
        self.widget.on(PARENT_ADDED, self.trackParent)
        
    def trackParent(self, widget=None, event=None):
        """ Track the parent widget """
        self.action = self.parentMenu.addAction(self.actionText)
        self.action.triggered.connect(self.triggered.emit)
        
    @property
    def parentMenu(self):
        """ Return the parent menu """
        return self.widget.parent.controller.menu
        
    @property
    def actionText(self):
        """ Return the parent menu """
        return self.widget.content.text if self.widget.content is not None else ''