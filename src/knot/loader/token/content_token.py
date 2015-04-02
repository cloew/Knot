from .token_roles import CONTENT
from .value.scope_value import ScopeValue

from knot.widget.content import Content

from kao_decorators import proxy_for

class ContentToken:
    """ Represents a widget's content from a knot file """
    ROLE = CONTENT
    
    @classmethod
    def isValidFor(cls, section):
        """ Return if this token is valid for the given section """
        return True
    
    def __init__(self, section):
        """ Initialize the Content Token """
        self.valueTokens = []
        text = section[0].strip()
        self.text = ' '.join([self.handle(piece) for piece in text.split()])
            
    def handle(self, piece):
        """ Handle the piece by storing the value token and return the proper placeholder string """
        text = piece
        if ScopeValue.isValidFor(piece):
            self.valueTokens.append(ScopeValue(piece))
            text = '{}'
        return text
        
    def build(self, scope):
        """ Return the Content """
        return Content(self.text, self.valueTokens, scope)
        
    def __repr__(self):
        return "<ContentToken:{0}>".format(self.value)