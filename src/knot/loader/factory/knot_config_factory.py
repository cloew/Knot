
class KnotConfigFactory:
    """ Factory for creating objects via a configuration for a type """
    
    def __init__(self, config, buildMethod):
        """ Initialize the factory with its config dictionary and the method to use to load """
        self.config = config
        self.build = buildMethod
        
    def isValidType(self, aType):
        """ Return if this type is avialable in the configuration """
        return aType in self.config