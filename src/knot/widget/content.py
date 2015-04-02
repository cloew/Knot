from knot.service_manager import ServiceManager
from knot.events.signal import Signal

class Content:
    """ Represents the content in a widget """
    
    def __init__(self, text, valueTokens, scope):
        """ Initialize the Content """
        self.textFormat = text
        self.valueTokens = valueTokens
        self.scope = scope
        self.changed = Signal()
        
        app = ServiceManager.getService('app')
        app.watch(self, 'text', self.changed.emit)
        
    @property
    def text(self):
        """ Return the current text for the Content """
        return self.textFormat.format(*[value.getValue(self.scope) for value in self.valueTokens])