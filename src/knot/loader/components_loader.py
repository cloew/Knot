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
        
    @smart_defaults
    def loadAll(self, tokens, scope=EvenIfNone(PerCall(KnotScope()))):
        """ Load all tokens from the given scope """
        return [self.load(token, scope=scope) for token in tokens if token.ROLE is WIDGET]
    
    @smart_defaults
    def load(self, widgetToken, scope=EvenIfNone(PerCall(KnotScope()))):
        """ Load the given widget token """
        return self.widgetLoader.load(widgetToken, scope=scope)