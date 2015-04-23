from .token_roles import WIDGET, CONTENT, ATTRIBUTE, MOD

class ChildTokenProcessor:
    """ Helper class to load the child tokens for a widget token """
    ROLE_HANDLER = {WIDGET: 'addChild',
                    CONTENT: 'setContent',
                    ATTRIBUTE: 'setAttribute',
                    MOD: 'addChild'}
    
    def __init__(self, parent, factory):
        """ Initialize the Child Token Processor with its parent """
        self.factory = factory
        self.parent = parent
        self.children = []
        self.attributes = {}
        self.content = None
    
    def process(self, section):
        """ Process the given section in the context of the given parent token """
        children = self.factory.loadAllTokens(section)
        self.processChildren(children)
        
    def processChildren(self, children):
        """ Process the children so they are stored correctly """
        for childToken in children:
            getattr(self, self.ROLE_HANDLER[childToken.ROLE])(childToken)
        
    def addChild(self, child):
        """ Add the child to the list of tracked child widgets """
        self.children.append(child)
        child.parent = self.parent
        
    def setContent(self, content):
        """ Set the child content """
        self.content = content
        
    def setAttribute(self, token):
        """ Set the attribute """
        self.attributes[token.attribute] = token