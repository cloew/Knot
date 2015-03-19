from .token_roles import WIDGET, CONTENT
from .parser.widget_type_parser import WidgetTypeParser

class WidgetToken:
    """ Represents a tokenized widget from a knot file """
    ROLE = WIDGET
    
    def __init__(self, section, factory):
        """ Intialize the Widget Token with the section it was loaded from """
        self.widgetType = WidgetTypeParser().find(section)
        
        self.children = []
        self.content = None
        children = factory.loadAllTokens(section[1:])
        self.processChildren(children)
        
    def processChildren(self, children):
        """ Process the children so theya re stored correctly """
        roleHandler = {WIDGET:self.addChild,
                       CONTENT: self.setContent}
        
        for childToken in children:
            roleHandler[childToken.ROLE](childToken)
        
    def addChild(self, child):
        """ Add the child to the list of tracked child widgets """
        self.children.append(child)
        
    def setContent(self, content):
        """ Set the child content """
        self.content = content
        
    def __repr__(self):
        return "<WidgetToken:{0},{1}, [{2}]>".format(self.widgetType, self.content, ", ".join([repr(child) for child in self.children]))