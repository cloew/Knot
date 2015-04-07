from .knot_list_parser import KnotListParser
from .value.value_factory import ValueFactory

class TypeToken:
    """ Represents a tokenized type to be used to load from a factory """
    
    @classmethod
    def loadAll(cls, text):
        """ Load all the type tokens from the text """
        return [cls(piece) for piece in KnotListParser().parse(text)]
    
    def __init__(self, text):
        """ Initialize the type """
        pieces = text.split('(', 1)
        self.type = pieces[0].strip()
        self.args, self.kwargs = self.getArguments(''.join(pieces[1:]))
        
    def getArguments(self, argumentText):
        """ Return the arguments """
        argumentText = argumentText.split(')')[0]
        argPieces = [arg.strip() for arg in KnotListParser().parse(argumentText) if arg.strip() != '']
        
        args = [ValueFactory.build(arg) for arg in argPieces if '=' not in arg]
        kwargs = {}
        for arg in argPieces:
            if '=' in arg:
                keyword, valueText = arg.split('=', maxsplit=1)
                kwargs[keyword] = ValueFactory.build(valueText)
        return args, kwargs
        
    def getArgumentValues(self, scope):
        """ Return the argument values """
        return [arg.getValue(scope) for arg in self.args]
        
    def getKeywordArgumentValues(self, scope):
        """ Return the keyword argument values """
        return {keyword:self.kwargs[keyword].getValue(scope) for keyword in self.kwargs}
        
    def build(self, factory, scope):
        """ Build this type form the factory """
        return factory.build(self.type, *self.getArgumentValues(scope), **self.getKeywordArgumentValues(scope))
        
    def __repr__(self):
        return "<TypeToken:{0}:{1}>".format(self.type, self.args)