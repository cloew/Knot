from kao_xobj import xobj_attrgetter

class ScopeValue:
    """ Represents a Value from the current scope """
             
    @classmethod
    def isValidFor(cls, valueText):
        """ Return if this class is valid for the given value text """
        return valueText.startswith('$.')
    
    def __init__(self, valueText):
        """ Initialize the value token """
        self.attrgetter = xobj_attrgetter(valueText.split('$.', 1)[1])
        
    def getValue(self, scope):
        """ Return the actual value of the given token """
        return self.attrgetter(scope)