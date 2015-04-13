from .child_token_processor import ChildTokenProcessor
from .token_roles import MOD
from .value.value_factory import ValueFactory
from knot.core.mods.for_loop import ForLoop

from kao_decorators import proxy_for

@proxy_for('processor', ['children'])
class ForLoopToken:
    """ Represents a tokenized for loop construct """
    ROLE = MOD
    
    @classmethod
    def isValidFor(cls, section):
        """ Return if this token is valid for the given section """
        firstLine = section[0].strip()
        return firstLine.startswith('@for')
    
    def __init__(self, section, factory):
        """ Initialize the For Loop Token """
        loopDef = section[0].strip()[5:]
        entryVarName, listVarName = loopDef.split(' in ', maxsplit=1)
        self.entryName = entryVarName.strip()
        self.listValueToken = ValueFactory.buildScopeValue(listVarName.strip())
        
        self.processor = ChildTokenProcessor(self, factory)
        self.processor.process(section[1:])
        
    def build(self, config, scope):
        """ Build this type from the config """
        return ForLoop(self.entryName, self.listValueToken.getValue(scope), config, self.children, scope)