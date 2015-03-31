from .token_roles import WIDGET, CONTENT, ATTRIBUTE
from .type_token import TypeToken

class WidgetToken:
    """ Represents a tokenized widget from a knot file """
    ROLE = WIDGET
    
    @classmethod
    def isValidFor(cls, section, config):
        """ Return if this token is valid for the given section """
        widgetType = cls.getWidgetType(section)
        return widgetType is not None and config.widgetFactory.isValidType(widgetType)
        
    @staticmethod
    def getWidgetType(section):
        """ Find the widget type in the given section """
        firstLine = section[0]
        pieces = firstLine.split()
        if len(pieces) == 1:
            return pieces[0].split('(')[0].strip()
        else:
            return None
    
    def __init__(self, section, factory):
        """ Intialize the Widget Token with the section it was loaded from """
        self.widgetType = TypeToken(section[0])
        
        self.children = []
        self.attributes = {}
        self.content = None
        children = factory.loadAllTokens(section[1:])
        self.processChildren(children)
        
    def processChildren(self, children):
        """ Process the children so theya re stored correctly """
        roleHandler = {WIDGET: self.addChild,
                       CONTENT: self.setContent,
                       ATTRIBUTE: self.setAttribute}
        
        for childToken in children:
            roleHandler[childToken.ROLE](childToken)
        
    def addChild(self, child):
        """ Add the child to the list of tracked child widgets """
        self.children.append(child)
        
    def setContent(self, content):
        """ Set the child content """
        self.content = content
        
    def setAttribute(self, token):
        """ Set the attribute """
        self.attributes[token.attribute] = token
        
    def __repr__(self):
        return "<WidgetToken:{0},{1}, [{2}]>".format(self.widgetType, self.content, ", ".join([repr(child) for child in self.children]))