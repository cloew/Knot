from .value_token import ValueToken

class TypeToken:
    """ Represents a tokenized type to be used to load from a factory """
    
    def __init__(self, text):
        """ Initialize the type """
        pieces = text.split('(', 1)
        self.type = pieces[0].strip()
        self.args = self.getArguments(''.join(pieces[1:]))
        
    def getArguments(self, argumentText):
        """ Return the arguments """
        return [ValueToken(arg.strip()) for arg in argumentText.split(')')[0].split(',') if arg.strip() != '']
        
    def build(self, factory):
        """ Build this type form the factory """
        return factory.build(self.type, *[arg.getValue() for arg in self.args])