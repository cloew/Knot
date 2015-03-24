from .token_roles import ATTRIBUTE
from .type_token import TypeToken

class AttributeToken:
    """ Represents a tokenized Knot attribute """
    ROLE = ATTRIBUTE
    
    @classmethod
    def isValidFor(cls, section):
        """ Return if this token is valid for the given section """
        return section[0].strip().startswith('@')
    
    def __init__(self, section):
        """ Initialize with the section for the attribute """
        pieces = section[0].split(maxsplit=1)
        self.attribute = pieces[0].split('@')[1]
        self.type = TypeToken(pieces[1])
        
    def __repr__(self):
        return "<AttributeToken:@{0}:{1}>".format(self.attribute, self.value)