from .parser.content_parser import ContentParser

class ContentToken:
    """ Represents a widget's content from a knot file """
    
    def __init__(self, section):
        """ Initialize the Content Token """
        self.value = ContentParser().find(section)
        
    def isContent(self):
        """ Return if this token is content """
        return True
        
    def __repr__(self):
        return "<ContentToken:{0}>".format(self.value)