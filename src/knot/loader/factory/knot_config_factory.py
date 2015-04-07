from ..config.config_helper import ConvertConfigsToDictionary
from kao_decorators import proxy_for
from smart_defaults import smart_defaults, PerCall

@proxy_for('config', ['update'])
class KnotConfigFactory:
    """ Factory for creating objects via a configuration for a type """
    
    @smart_defaults
    def __init__(self, configs=PerCall([])):
        """ Initialize the factory with its configs """
        self.config = ConvertConfigsToDictionary(configs)
        
    def build(self, requestedType, *args, **kwargs):
        """ Build the object for the requested type """
        return self.config[requestedType].build(*args, **kwargs)
        
    def isValidType(self, aType):
        """ Return if this type is avialable in the configuration """
        return aType in self.config
        
    def __deepcopy__(self, memo_dict):
        """ Return a deep copy of this object """
        return KnotConfigFactory(self.config.values())