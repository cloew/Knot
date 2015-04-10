from .scope_getter import GetScopeFor
from .widget_loader import WidgetLoader
from .token.token_roles import WIDGET
from knot.scope.knot_scope import KnotScope

from smart_defaults import smart_defaults, EvenIfNone, PerCall

class ComponentsLoader:
    """ Helper class to load components from knot tokens """
    
    def __init__(self, config):
        """ Initialize the loader with the configuration to use """
        self.config = config
        self.widgetLoader = WidgetLoader(self.config)
        
    def loadAll(self, tokens, scope=None, onto=None):
        """ Load all tokens from the given scope """
        scope = self.getScope(scope, onto)
        children = [self.load(token, scope=scope) for token in tokens if token.ROLE is WIDGET]
        
        if onto is not None:
            self.attachChildren(onto, children)
            
        return children
    
    @smart_defaults
    def load(self, widgetToken, scope=EvenIfNone(PerCall(KnotScope()))):
        """ Load the given widget token """
        return self.widgetLoader.load(widgetToken, scope=scope)
        
    def getScope(self, scope, widget):
        """ Return the proper scope to use """
        return scope if scope is not None else GetScopeFor(widget)
        
    def attachChildren(self, widget, children):
        """ Attach children to the parent widget """
        for child in children:
            widget.addChild(child)