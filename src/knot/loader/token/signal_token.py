from .knot_list_parser import KnotListParser
from .value.value_factory import ValueFactory

from knot.core.mods.attach_to_signal import AttachToSignal

class SignalToken:
    """ Represents a tokenized Signal callback """
    
    def __init__(self, section, children):
        """ Initialize with the section for the signal """
        pieces = section[0].split(maxsplit=1)
        self.signalName, valuesText = [piece.strip() for piece in pieces[1].split('->')]
        self.values = [ValueFactory.buildScopeValue(valueText) for valueText in KnotListParser().parse(valuesText)]
        
    def build(self, config, scope):
        """ Build this type from the config """
        return AttachToSignal(self.signalName, [value.getValue(scope) for value in self.values])
        
    def __repr__(self):
        return "<SignalToken:{0}:{1}>".format(self.signalName, self.values)