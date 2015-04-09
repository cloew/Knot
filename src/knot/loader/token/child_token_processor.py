from .token_roles import WIDGET, CONTENT, ATTRIBUTE, SIGNAL, STYLE

class ChildTokenProcessor:
    """ Helper class to load the child tokens for a widget token """
    
    def __init__(self, parent, factory):
        """ Initialize the Child Token Processor with its parent """
        self.factory = factory
        self.roleHandler = {WIDGET: parent.addChild,
                            CONTENT: parent.setContent,
                            SIGNAL: parent.setSignal,
                            STYLE: parent.setStyle,
                            ATTRIBUTE: parent.setAttribute}
    
    def process(self, section):
        """ Process the given section in the context of the given parent token """
        children = self.factory.loadAllTokens(section)
        self.processChildren(children)
        
    def processChildren(self, children):
        """ Process the children so theya re stored correctly """
        for childToken in children:
            self.roleHandler[childToken.ROLE](childToken)