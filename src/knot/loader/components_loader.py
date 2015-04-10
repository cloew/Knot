from .scope_getter import GetScopeFor
from .widget_loader import WidgetLoader
from .token.token_roles import MOD, WIDGET

from knot.widget.base_widget import BaseWidget
from knot.scope.knot_scope import KnotScope

from smart_defaults import smart_defaults, EvenIfNone, PerCall

class ComponentsLoader:
    """ Helper class to load components from knot tokens """
    LOAD_METHODS = {WIDGET: 'loadWidget',
                    MOD: 'loadMod'}
    
    def __init__(self, config):
        """ Initialize the loader with the configuration to use """
        self.config = config
        self.widgetLoader = WidgetLoader(self.config)
        
    def loadAll(self, tokens, scope=None, onto=None):
        """ Load all tokens from the given scope """
        scope = GetScopeFor(onto, currentScope=scope)
        children = [self.load(token, scope=scope) for token in tokens if token.ROLE in self.LOAD_METHODS]
        
        if onto is not None:
            self.attachChildren(onto, children)
            
        return children
    
    @smart_defaults
    def load(self, token, scope=EvenIfNone(PerCall(KnotScope()))):
        """ Load the given token """
        return getattr(self, self.LOAD_METHODS[token.ROLE])(token, scope)
        
    def loadWidget(self, widgetToken, scope):
        """ Load the given widget token """
        widget = self.widgetLoader.load(widgetToken, scope)
        config = widgetToken.getChildConfig(self.config)
        ComponentsLoader(config).loadAll(widgetToken.children, scope=scope, onto=widget)
        return widget
        
    def loadMod(self, modToken, scope):
        """ Load the given mod token """
        return modToken.build(self.config, scope)
        
    def attachChildren(self, widget, children):
        """ Attach children to the parent widget """
        for child in children:
            if isinstance(child, BaseWidget):
                widget.addChild(child)
            else:
                widget.addMod(child)