from .attributes import POSITION, SIZING
from .attribute_loader import AttributeLoader
from .factory.widget_factory import WidgetFactory

class WidgetLoader:
    """ Helper class to load widgets from knot tokens """
    
    def load(self, widgetToken):
        """ Load the given widget token """
        widgetType = widgetToken.widgetType
        content = widgetToken.content.value if widgetToken.content is not None else None
        
        attrLoader = AttributeLoader()
        positioning = attrLoader.load(POSITION, widgetToken.attributes[POSITION]) if POSITION in widgetToken.attributes else None
        sizing = attrLoader.load(SIZING, widgetToken.attributes[SIZING]) if SIZING in widgetToken.attributes else None
        
        widget = WidgetFactory.build(widgetType, content, positioning=positioning, sizing=sizing)
        
        for childToken in widgetToken.children:
            child = self.load(childToken)
            widget.addChild(child)
        return widget