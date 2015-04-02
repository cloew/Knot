
class Content:
    """ Represents the content in a widget """
    
    def __init__(self, text, valueTokens, scope):
        """ Initialize the Content """
        self.textFormat = text
        self.valueTokens = valueTokens
        self.scope = scope
        
    @property
    def text(self):
        """ Return the current text for the Content """
        return self.textFormat.format(*[value.getValue(self.scope) for value in self.valueTokens])