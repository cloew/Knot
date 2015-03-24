
class TypeToken:
    """ Represents a tokenized type to be used to load from a factory """
    
    def __init__(self, text):
        """ Initialize the type """
        self.type = text.split('(', 1)[0]
        self.type = self.type.strip()
        
    def build(self, factory):
        """ Build this type form the factory """
        return factory.build(self.type)