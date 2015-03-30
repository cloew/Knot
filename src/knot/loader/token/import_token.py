from .token_roles import IMPORT

class ImportToken:
    """ Represents a Tokenized Knot package import """
    ROLE = IMPORT
    
    @classmethod
    def isValidFor(cls, line):
        """ Return if this token is valid for the given section """
        return line.startswith('import')
    
    def __init__(self, line):
        """ Initialize with the line for the import """
        self.package = line.split('import ')[1].strip()
        
    def __repr__(self):
        return "<ImportToken:{0}>".format(self.package)