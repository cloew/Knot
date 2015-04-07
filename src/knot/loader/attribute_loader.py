from .attributes import POSITION, SIZING

class AttributeLoader:
    """ Helper class to load attributes from knot tokens """
    
    def __init__(self, config):
        """ Initialize the loader with the configuration to use """
        self.config = config
    
    def load(self, attribute, attrToken, scope):
        """ Load the given attribute token """
        factory = self.config.attributesFactory[attribute]
        return [type.build(factory, scope) for type in attrToken.types]