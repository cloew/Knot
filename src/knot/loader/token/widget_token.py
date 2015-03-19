from .parser.widget_type_parser import WidgetTypeParser

class WidgetToken:
    """ Represents a tokenized widget from a knot file """
    
    def __init__(self, section, factory):
        """ Intialize the Widget Token with the section it was loaded from """
        self.widgetType = WidgetTypeParser().find(section)
        
        children = factory.loadAllTokens(section[1:])
        self.processChildren(children)
        
    def processChildren(self, children):
        """ Process the children so theya re stored correctly """
        self.children = [child for child in children if not child.isContent()]
        self.content = self.getContent(children)
        
    def getContent(self, children):
        """ Return the content for this Widget """
        contentChildren = [child for child in children if child.isContent()]
        if len(contentChildren) == 1:
            self.checkForBadContent(contentChildren, children)
            return contentChildren[0]
        else:
            return None
        
    def checkForBadContent(self, contentChildren, children):
        """ Ensure the Widget matches the proper constraints on content """
        if len(contentChildren) > 1:
            pass # raise some error for having multiple unknown widgets..?
        elif len(children) > 1:
            pass # raise error for having content and children elements
            
    def isContent(self):
        """ Return that this token is not a content token """
        return False
        
    def __repr__(self):
        return "<WidgetToken:{0},{1}, [{2}]>".format(self.widgetType, self.content, ", ".join([repr(child) for child in self.children]))