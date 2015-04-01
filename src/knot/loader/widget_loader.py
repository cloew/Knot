from .attributes import POSITION, SIZING
from .attribute_loader import AttributeLoader
from .scope_getter import GetScopeFor

class WidgetLoader:
    """ Helper class to load widgets from knot tokens """
    
    def __init__(self, config):
        """ Initialize the loader with the configuration to use """
        self.config = config
    
    def load(self, widgetToken, scope=None):
        """ Load the given widget token """
        attrLoader = AttributeLoader(self.config)
        positioning = attrLoader.load(POSITION, widgetToken.attributes[POSITION], scope) if POSITION in widgetToken.attributes else None
        sizing = attrLoader.load(SIZING, widgetToken.attributes[SIZING], scope) if SIZING in widgetToken.attributes else None
        
        widget = widgetToken.build(self.config.widgetFactory, scope, positioning=positioning, sizing=sizing)
        
        scope = GetScopeFor(widget, currentScope=scope)
        for childToken in widgetToken.children:
            child = self.load(childToken, scope=scope)
            widget.addChild(child)
        return widget