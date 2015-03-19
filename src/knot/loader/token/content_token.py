from .token_roles import CONTENT

class ContentToken:
    """ Represents a widget's content from a knot file """
    ROLE = CONTENT
    
    @classmethod
    def isValidFor(cls, section):
        """ Return if this token is valid for the given section """
        return True
    
    def __init__(self, section):
        """ Initialize the Content Token """
        self.value = section[0].strip()
        
    def isContent(self):
        """ Return if this token is content """
        return True
        
    def __repr__(self):
        return "<ContentToken:{0}>".format(self.value)