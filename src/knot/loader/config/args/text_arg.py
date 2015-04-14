
class TextArg:
    """ Represents an argument that receives the plain text """
    REQUIRES_TEXT = True
        
    def build(self, piece, section, children, config, scope):
        """ Return the text """
        return piece