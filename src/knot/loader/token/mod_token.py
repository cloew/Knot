from .child_token_processor import ChildTokenProcessor
from .token_roles import MOD

from kao_decorators import proxy_for

@proxy_for('processor', ['children'])
class ModToken:
    """ Represents a token for a mod """
    ROLE = MOD
    
    @classmethod
    def isValidFor(cls, section):
        """ Return if this token is valid for the given section """
        firstLine = section[0].strip()
        return firstLine.startswith('@')
    
    def __init__(self, section, factory):
        """ Initialize the For Loop Token """
        self.parent = None
        self.modType = section[0].strip()[1:].split(maxsplit=1)[0]
        self.section = section
        self.processor = ChildTokenProcessor(self.parent, factory)
        self.processor.process(section[1:])
        
    def build(self, config, scope):
        """ Build this type from the config """
        return config.modFactory.build(self.modType, self.section, self.children, config, scope)
        
    def __repr__(self):
        """ Return the string representation """
        return "<ModToken:{0}>".format(self.modType)