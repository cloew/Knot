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
        self.args = self.getArguments(''.join(pieces[1:]))
        
    def getArguments(self, argumentText):
        """ Return the arguments """
        argumentText = argumentText.split(')')[0]
        return [ValueFactory.build(arg.strip()) for arg in KnotListParser().parse(argumentText) if arg.strip() != '']
        
    def getArgumentValues(self, scope):
        """ Return the argument values """
        return [arg.getValue(scope) for arg in self.args]
        
    def build(self, factory, scope):
        """ Build this type form the factory """
        return factory.build(self.type, *self.getArgumentValues(scope))
        
    def __repr__(self):
        return "<TypeToken:{0}:{1}>".format(self.type, self.args)