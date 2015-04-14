
class ConfigArg:
    """ Represents an argument that is the current configuration """
    REQUIRES_TEXT = False
        
    def build(self, piece, section, children, config, scope):
        """ Return the config """
        return config