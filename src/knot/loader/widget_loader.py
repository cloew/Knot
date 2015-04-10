from .attributes import POSITION, SIZING
from .attribute_loader import AttributeLoader
from .scope_getter import GetScopeFor

class WidgetLoader:
    """ Helper class to load widgets from knot tokens """
    
    def __init__(self, config):
        """ Initialize the loader with the configuration to use """
        self.config = config
    
    def load(self, widgetToken, scope):
        """ Load the given widget token """
        attrLoader = AttributeLoader(self.config)
        positionings = attrLoader.load(POSITION, widgetToken.attributes[POSITION], scope) if POSITION in widgetToken.attributes else None
        sizings = attrLoader.load(SIZING, widgetToken.attributes[SIZING], scope) if SIZING in widgetToken.attributes else None
        
        return widgetToken.build(self.config.widgetFactory, scope, positionings=positionings, sizings=sizings)