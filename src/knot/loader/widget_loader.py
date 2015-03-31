from .attributes import POSITION, SIZING
from .attribute_loader import AttributeLoader

class WidgetLoader:
    """ Helper class to load widgets from knot tokens """
    
    def __init__(self, config):
        """ Initialize the loader with the configuration to use """
        self.config = config
    
    def load(self, widgetToken):
        """ Load the given widget token """
        widgetType = widgetToken.widgetType
        content = widgetToken.content.value if widgetToken.content is not None else None
        
        attrLoader = AttributeLoader(self.config)
        positioning = attrLoader.load(POSITION, widgetToken.attributes[POSITION]) if POSITION in widgetToken.attributes else None
        sizing = attrLoader.load(SIZING, widgetToken.attributes[SIZING]) if SIZING in widgetToken.attributes else None
        
        widget = self.config.widgetFactory.build(widgetType.type, content, *widgetType.arguments, positioning=positioning, sizing=sizing)
        
        for childToken in widgetToken.children:
            child = self.load(childToken)
            widget.addChild(child)
        return widget