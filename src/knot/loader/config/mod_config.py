from kao_modules import NamespacedClass

class ModConfig:
    """ Represents the configuration for a widget mod """
    
    def __init__(self, name, tokenClass):
        """ Initialize the mod config with its name and token class """
        self.name = name
        self.tokenClass = NamespacedClass(tokenClass)
        
    def build(self, section, children, config, scope):
        """ Return the proper widget object """
        token = self.tokenClass.instantiate(section, children)
        return token.build(config, scope)