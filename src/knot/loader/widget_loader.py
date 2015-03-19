from .factory.widget_factory import WidgetFactory

class WidgetLoader:
    """ Helper class to load widgets from knot tokens """
    
    def load(self, widgetToken):
        """ Load the given widget token """
        widgetType = widgetToken.widgetType
        content = widgetToken.content.value if widgetToken.content is not None else None
        
        widget = WidgetFactory.build(widgetType, content)
        for childToken in widgetToken.children:
            child = self.load(childToken)
            widget.addChild(child)
        return widget