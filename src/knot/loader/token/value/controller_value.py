from knot.scope.scoped_value import ScopedValue

class ControllerValue:
    """ Represents a Value from the current scope's controller """
             
    @classmethod
    def isValidFor(cls, valueText):
        """ Return if this class is valid for the given value text """
        return valueText.startswith('$.')
    
    def __init__(self, valueText):
        """ Initialize the value token """
        self.attrName = "controller.{0}".format(valueText.split('$.', 1)[1])
        
    def getValue(self, scope):
        """ Return the actual value of the given token """
        return ScopedValue(scope, self.attrName)