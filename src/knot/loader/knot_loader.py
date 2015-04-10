from .components_loader import ComponentsLoader
from .import_loader import ImportLoader
from .tokenizer import Tokenizer
from .config.loader_config import LoaderConfig

class KnotLoader:
    """ Loads Knot files and converts them to the proper widget tree """
    
    def __init__(self, filename):
        """ Initialize with the file to load from """
        self.tokenizer = Tokenizer(filename)
        self.config = LoaderConfig()
        self.componentsLoader = ComponentsLoader(self.config)
        self.importLoader = ImportLoader(self.config)
        
    def load(self, scope=None, onto=None):
        """ Load the widgets from the filename """
        importTokens, componentTokens = self.tokenizer.tokenize()
        self.importLoader.loadAll(importTokens)
        return self.componentsLoader.loadAll(componentTokens, scope=scope, onto=onto)