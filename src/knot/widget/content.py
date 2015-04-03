from knot.service_manager import ServiceManager
from knot.events.signal import Signal

class Content:
    """ Represents the content in a widget """
    
    def __init__(self, text, scopedValues):
        """ Initialize the Content """
        self.textFormat = text
        self.scopedValues = scopedValues
        self.changed = Signal()
        
    def addWatch(self, app):
        """ Add the watch for this content to the app """
        app.watch(self, 'text', self.changed.emit)
        
    @property
    def text(self):
        """ Return the current text for the Content """
        return self.textFormat.format(*[value.get() for value in self.scopedValues])