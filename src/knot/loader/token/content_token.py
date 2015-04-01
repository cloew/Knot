from .token_roles import CONTENT
from .value.content_value import ContentValue
from .value.scope_value import ScopeValue

from kao_decorators import proxy_for

@proxy_for('value', ['getValue'])
class ContentToken:
    """ Represents a widget's content from a knot file """
    ROLE = CONTENT
    
    @classmethod
    def isValidFor(cls, section):
        """ Return if this token is valid for the given section """
        return True
    
    def __init__(self, section):
        """ Initialize the Content Token """
        text = section[0].strip()
        self.value = None
        if ScopeValue.isValidFor(text):
            self.value = ScopeValue(text)
        else:
            self.value = ContentValue(text)
        
    def __repr__(self):
        return "<ContentToken:{0}>".format(self.value)