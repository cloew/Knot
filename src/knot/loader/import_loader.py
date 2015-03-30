
class ImportLoader:
    """ Helper class to perform imports from knot tokens """
    
    def __init__(self, config):
        """ Initialize the loader with the configuration to use """
        self.config = config
    
    def load(self, importToken):
        """ Load the given import token """
        self.config.importPackage(importToken.package)