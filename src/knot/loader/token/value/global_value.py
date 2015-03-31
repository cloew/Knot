from knot.dimensions import HORIZONTAL, VERTICAL
from knot.sides import LEFT, RIGHT, TOP, BOTTOM

class GlobalValue:
    """ Represents a tokenized value to retrieve from the scope """
    GLOBAL_SCOPE = {"HORIZONTAL":HORIZONTAL,
                    "VERTICAL":VERTICAL,
                    "LEFT":LEFT,
                    "RIGHT":RIGHT,
                    "TOP":TOP,
                    "BOTTOM":BOTTOM}
             
    @classmethod
    def isValidFor(cls, valueText):
        """ Return if this class is valid for the given value text """
        return valueText in cls.GLOBAL_SCOPE
    
    def __init__(self, valueText):
        """ Initialize the value token """
        self.valueText = valueText
        
    def getValue(self):
        """ Return the actual value of the given token """
        return self.GLOBAL_SCOPE[self.valueText]