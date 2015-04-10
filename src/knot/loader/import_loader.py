
class ImportLoader:
    """ Helper class to perform imports from knot tokens """
    
    def __init__(self, config):
        """ Initialize the loader with the configuration to use """
        self.config = config
    
    def loadAll(self, tokens):
        """ Load the given import tokens """
        for token in tokens:
            self.load(token)
    
    def load(self, importToken):
        """ Load the given import token """
        self.config.importPackage(importToken.package)