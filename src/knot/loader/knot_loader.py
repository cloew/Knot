from .components_loader import ComponentsLoader
from .import_loader import ImportLoader
from .widget_loader import WidgetLoader
from .scope_getter import GetScopeFor
from .tokenizer import Tokenizer
from .config.loader_config import LoaderConfig

from .token.token_roles import IMPORT, WIDGET

from knot.scope.knot_scope import KnotScope
from smart_defaults import smart_defaults, EvenIfNone, PerCall

class KnotLoader:
    """ Loads Knot files and converts them to the proper widget tree """
    
    def __init__(self, filename):
        """ Initialize with the file to load from """
        self.tokenizer = Tokenizer(filename)
        self.config = LoaderConfig()
        self.componentsLoader = ComponentsLoader(self.config)
        self.importLoader = ImportLoader(self.config)
        
    def loadOnto(self, widget):
        """ Load the contents of the given file and place them on the given widget """
        children = self.load(scope=GetScopeFor(widget))
        for child in children:
            widget.addChild(child)
        
    def load(self, scope=None):
        """ Load the widgets from the filename """
        importTokens, componentTokens = self.tokenizer.tokenize()
        # self.loadImports(importTokens)
        self.importLoader.loadAll(importTokens)
        return self.componentsLoader.loadAll(componentTokens, scope=scope)
        
    def loadImports(self, tokens):
        """ Load the widget section of the Knot File """
        return [importLoader.load(token) for token in tokens if token.ROLE is IMPORT]