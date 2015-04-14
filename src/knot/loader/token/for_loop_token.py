from .value.value_factory import ValueFactory
from knot.core.mods.for_loop import ForLoop

class ForLoopToken:
    """ Represents a tokenized for loop construct """
    
    def __init__(self, section, children):
        """ Initialize the For Loop Token """
        loopDef = section[0].strip()[5:]
        entryVarName, listVarName = loopDef.split(' in ', maxsplit=1)
        self.entryName = entryVarName.strip()
        self.listValueToken = ValueFactory.buildScopeValue(listVarName.strip())
        self.children = children
        
    def build(self, config, scope):
        """ Build this type from the config """
        return ForLoop(self.entryName, self.listValueToken.getValue(scope), config, self.children, scope)