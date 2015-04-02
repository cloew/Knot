from .token_roles import WIDGET, CONTENT, ATTRIBUTE, SIGNAL
from .type_token import TypeToken

class WidgetToken:
    """ Represents a tokenized widget from a knot file """
    ROLE = WIDGET
    
    @classmethod
    def isValidFor(cls, section, config):
        """ Return if this token is valid for the given section """
        widgetType = cls.getWidgetType(section)
        return widgetType is not None and config.widgetFactory.isValidType(widgetType.type)
        
    @staticmethod
    def getWidgetType(section):
        """ Find the widget type in the given section """
        firstLine = section[0]
        return TypeToken(firstLine)
    
    def __init__(self, section, factory):
        """ Intialize the Widget Token with the section it was loaded from """
        self.widgetType = self.getWidgetType(section)
        
        self.children = []
        self.signals = []
        self.attributes = {}
        self.content = None
        children = factory.loadAllTokens(section[1:])
        self.processChildren(children)
        
    def processChildren(self, children):
        """ Process the children so theya re stored correctly """
        roleHandler = {WIDGET: self.addChild,
                       CONTENT: self.setContent,
                       SIGNAL: self.setSignal,
                       ATTRIBUTE: self.setAttribute}
        
        for childToken in children:
            roleHandler[childToken.ROLE](childToken)
        
    def addChild(self, child):
        """ Add the child to the list of tracked child widgets """
        self.children.append(child)
        
    def setContent(self, content):
        """ Set the child content """
        self.content = content
        
    def setSignal(self, signal):
        """ Set the child content """
        self.signals.append(signal)
        
    def setAttribute(self, token):
        """ Set the attribute """
        self.attributes[token.attribute] = token
        
    def build(self, factory, scope, **kwargs):
        """ Build this type form the factory """
        content = self.content.getValue(scope) if self.content is not None else None
        return factory.build(self.widgetType.type, content, *self.widgetType.getArgumentValues(scope), **kwargs)
        
    def __repr__(self):
        return "<WidgetToken:{0},{1}, [{2}]>".format(self.widgetType, self.content, ", ".join([repr(child) for child in self.children]))