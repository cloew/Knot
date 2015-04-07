from .token_roles import WIDGET, CONTENT, ATTRIBUTE, SIGNAL, STYLE

class ChildTokenProcessor:
    """ Helper class to load the child tokens for a widget token """
    
    def __init__(self, parent, factory):
        """ Initialize the Child Token Processor with its parent """
        self.parent = parent
        self.config = self.getChildConfig(factory)
        self.childFactory = factory.__class__(self.config)
    
    def process(self, section):
        """ Process the given section in the context of the given parent token """
        children = self.childFactory.loadAllTokens(section)
        self.processChildren(children)
        
    def getChildConfig(self, factory):
        """ Return the config to be used for any child widgets """
        config = factory.config
        widgetConfig = factory.config.widgetFactory.config[self.parent.widgetType.type]
        if len(widgetConfig.childWidgetConfigs) > 0:
            config = factory.config.copy(additionalWidgetConfigs=widgetConfig.childWidgetConfigs)
        return config
        
    def processChildren(self, children):
        """ Process the children so theya re stored correctly """
        roleHandler = {WIDGET: self.parent.addChild,
                       CONTENT: self.parent.setContent,
                       SIGNAL: self.parent.setSignal,
                       STYLE: self.parent.setStyle,
                       ATTRIBUTE: self.parent.setAttribute}
        
        for childToken in children:
            roleHandler[childToken.ROLE](childToken)