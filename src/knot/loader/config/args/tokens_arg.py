
class TokensArg:
    """ Represents an argument that is the child token list """
    REQUIRES_TEXT = False
        
    def build(self, piece, section, children, config, scope):
        """ Return the children tokens """
        return children