
class KnotConfigFactory:
    """ Factory for creating objects via a configuration for a type """
    
    def __init__(self, configs):
        """ Initialize the factory with its configs """
        self.config = {config.name:config for config in configs}
        
    def build(self, requestedType, *args, **kwargs):
        """ Build the object for the requested type """
        return self.config[requestedType].build(*args, **kwargs)
        
    def isValidType(self, aType):
        """ Return if this type is avialable in the configuration """
        return aType in self.config