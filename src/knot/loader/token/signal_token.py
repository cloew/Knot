from .knot_list_parser import KnotListParser
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
        self.signalName, valuesText = [piece.strip() for piece in pieces[1].split('->')]
        self.values = [ScopeValue(valueText) for valueText in KnotListParser().parse(valuesText)]
        
    def attach(self, controller, scope):
        """ Attach the signal and its callback """
        signal = getattr(controller, self.signalName)
        for value in self.values:
            signal.register(value.getValue(scope).get())
        
    def __repr__(self):
        return "<ScopeToken:{0}:{1}>".format(self.signalName, self.values)