
class ScopeArg:
    """ Represents an argument that is the current scope """
    REQUIRES_TEXT = False
        
    def build(self, piece, section, children, config, scope):
        """ Return the scope """
        return scope