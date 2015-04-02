from .token_roles import SIGNAL
from .value.scope_value import ScopeValue

class SignalToken:
    """ Represents a tokenized Signal callback """
    ROLE = SIGNAL
    
    @classmethod
    def isValidFor(cls, section):
        """ Return if this token is valid for the given section """
        return section[0].strip().startswith('@when')
    
    def __init__(self, section):
        """ Initialize with the section for the signal """
        pieces = section[0].split(maxsplit=1)
        self.signalName, valueText = [piece.strip() for piece in pieces[1].split('->')]
        self.value = ScopeValue(valueText)
        
    def __repr__(self):
        return "<ScopeToken:{0}:{1}>".format(self.signalName, self.value)