from .token_roles import ATTRIBUTE
from .type_token import TypeToken

class AttributeToken:
    """ Represents a tokenized Knot attribute """
    ROLE = ATTRIBUTE
    
    @classmethod
    def isValidFor(cls, section):
        """ Return if this token is valid for the given section """
        firstLine = section[0].strip()
        return firstLine.startswith('@position') or firstLine.startswith('@size')
    
    def __init__(self, section, factory=None):
        """ Initialize with the section for the attribute """
        pieces = section[0].split(maxsplit=1)
        self.attribute = pieces[0].split('@')[1]
        self.types = TypeToken.loadAll(pieces[1])
        
    def __repr__(self):
        return "<AttributeToken:@{0}:{1}>".format(self.attribute, self.value)