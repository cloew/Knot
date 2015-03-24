from knot.dimensions import HORIZONTAL, VERTICAL
from knot.sides import LEFT, RIGHT, TOP, BOTTOM

class ValueToken:
    """ Represents a tokenized value to retrieve from the scope """
    GLOBAL_SCOPE = {"HORIZONTAL":HORIZONTAL,
                    "VERTICAL":VERTICAL,
                    "LEFT":LEFT,
                    "RIGHT":RIGHT,
                    "TOP":TOP,
                    "BOTTOM":BOTTOM}
    
    def __init__(self, varName):
        """ Initialize the value token """
        self.varName = varName
        
    def getValue(self):
        """ Return the actual value of the given token """
        return self.GLOBAL_SCOPE[self.varName]