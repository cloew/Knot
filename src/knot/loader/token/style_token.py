from .knot_list_parser import KnotListParser
from .token_roles import STYLE
from .value.scope_value import ScopeValue

class StyleToken:
    """ Represents a tokenized Style dictionary """
    ROLE = STYLE
    
    @classmethod
    def isValidFor(cls, section):
        """ Return if this token is valid for the given section """
        return section[0].strip().startswith('@style')
    
    def __init__(self, section):
        """ Initialize with the section for the style """
        attribute, self.styling = section[0].split(maxsplit=1)
        
    def __repr__(self):
        return "<StyleToken:{0}>".format(self.styling)