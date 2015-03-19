from .token_roles import ATTRIBUTE

class AttributeToken:
    """ Represents a tokenized Knot attribute """
    ROLE = ATTRIBUTE
    
    def __init__(self, section):
        """ Initialize with the section for the attribute """
        pieces = section[0].split()
        self.attribute = pieces[0].split('@')[1]
        self.value = pieces[1]
        
    def __repr__(self):
        return "<AttributeToken:@{0}:{1}>".format(self.attribute, self.value)