from .value.value_factory import ValueFactory

class TypeToken:
    """ Represents a tokenized type to be used to load from a factory """
    
    def __init__(self, text):
        """ Initialize the type """
        pieces = text.split('(', 1)
        self.type = pieces[0].strip()
        self.args = self.getArguments(''.join(pieces[1:]))
        
    def getArguments(self, argumentText):
        """ Return the arguments """
        return [ValueFactory.build(arg.strip()) for arg in argumentText.split(')')[0].split(',') if arg.strip() != '']
        
    def getArgumentValues(self, scope):
        """ Return the argument values """
        return [arg.getValue(scope) for arg in self.args]
        
    def build(self, factory, scope):
        """ Build this type form the factory """
        return factory.build(self.type, *self.getArgumentValues(scope))