from knot import KnotService
from knot.events.signal import Signal

class Content:
    """ Represents the content in a widget """
    app = KnotService('app')
    
    def __init__(self, text, scopedValues):
        """ Initialize the Content """
        self.textFormat = text
        self.scopedValues = scopedValues
        self.changed = Signal()
        
        if len(self.scopedValues) > 0:
            self.app.watch(self, 'text', self.changed.emit)
        
    @property
    def text(self):
        """ Return the current text for the Content """
        return self.textFormat.format(*[value.get() for value in self.scopedValues])
        
    @property
    def scope(self):
        """ The scope used for the content """
        return self.scopedValues[0].scope if len(self.scopedValues) > 0 else None
        
    @scope.setter
    def scope(self, newScope):
        """ Set the scope for all the scoped values to use the new scope """
        for scopedValue in self.scopedValues:
            scopedValue.scope = newScope