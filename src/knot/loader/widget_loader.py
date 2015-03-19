from knot.widget_factory import BuildWidget

class WidgetLoader:
    """ Helper class to load widgets from knot tokens """
    
    def load(self, widgetToken):
        """ Load the given widget token """
        widgetType = widgetToken.widgetType
        content = widgetToken.content.value if widgetToken.content is not None else None
        
        widget = BuildWidget(widgetType, content)
        for childToken in widgetToken.children:
            child = self.load(childToken)
            widget.addChild(child)
        return widget