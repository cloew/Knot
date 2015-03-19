from .token_roles import ATTRIBUTE

class AttributeToken:
    """ Represents a tokenized Knot attribute """
    ROLE = ATTRIBUTE
    
    def __init__(self, section):
        """ Initialize with the section for the attribute """
        pieces = section[0].split()
        self.attribute = pieces.split('@')[1]
        self.value = pieces[1]