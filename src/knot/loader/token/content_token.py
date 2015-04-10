from .token_roles import CONTENT
from .value.value_factory import ValueFactory

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
        valueToken = ValueFactory.buildScopeValue(piece)
        if valueToken is not None:
            self.valueTokens.append(valueToken)
            text = '{}'
        return text
        
    def build(self, scope):
        """ Return the Content """
        return Content(self.text, [token.getValue(scope) for token in self.valueTokens])
        
    def __repr__(self):
        return "<ContentToken:{0}, {1}>".format(self.text, self.valueTokens)