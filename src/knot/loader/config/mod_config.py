from kao_modules import NamespacedClass

class ModConfig:
    """ Represents the configuration for a widget mod """
    
    def __init__(self, name, tokenClass, token=None, args=[]):
        """ Initialize the mod config with its name and token class """
        self.name = name
        self.tokenClass = NamespacedClass(tokenClass)
        
        if token is not None:
            self.tokenPieces = [tokenPiece for tokenPiece in token.split('$arg') if tokenPiece.strip() != '']
        else:
            self.tokenPieces = []
        self.args = args
        
    def build(self, section, children, config, scope):
        """ Return the proper widget object """
        args = self.getArguments(section, children, config, scope)
        return self.tokenClass.instantiate(*args)
        
    def getArguments(self, section, children, config, scope):
        """ Return the arguments """
        pieces = self.getArgTexts(section)
        index = 0
        
        values = []
        for arg in self.args:
            if arg.REQUIRES_TEXT:
                piece = pieces[index]
                value = arg.build(piece, section, children, config, scope)
                values.append(value)
                index += 1
            else:
                value = arg.build('', section, children, config, scope)
                values.append(value)
        return values
            
    def getArgTexts(self, section):
        """ Return the portions of text that correspond to each argument """
        firstLine = section[0].strip()
        content = firstLine.split(self.name, maxsplit=1)[1].strip()
        
        pieces = []
        rest = content
        for tokenPiece in self.tokenPieces:
            piece, rest = rest.split(tokenPiece)
            pieces.append(piece.strip())
        pieces.append(rest.strip())
        return pieces
        