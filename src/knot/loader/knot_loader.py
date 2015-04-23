from .components_loader import ComponentsLoader
from .import_loader import ImportLoader
from .tokenizer import Tokenizer
# from .config.loader_config import LoaderConfig

class KnotLoader:
    """ Loads Knot files and converts them to the proper widget tree """
    
    def __init__(self, filename, config):
        """ Initialize with the file to load from """
        self.tokenizer = Tokenizer(filename)
        # self.config = LoaderConfig()
        self.componentsLoader = ComponentsLoader(config)
        self.importLoader = ImportLoader(config)
        
    def load(self, onto=None):
        """ Load the widgets from the filename """
        importTokens, componentTokens = self.tokenizer.tokenize()
        self.importLoader.loadAll(importTokens)
        return self.componentsLoader.loadAll(componentTokens, onto=onto)