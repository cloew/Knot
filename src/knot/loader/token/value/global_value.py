from knot.dimensions import HORIZONTAL, VERTICAL
from knot.directions import L2R, R2L, T2B, B2T
from knot.sides import LEFT, RIGHT, TOP, BOTTOM

class GlobalValue:
    """ Represents a tokenized global value """
    GLOBAL_SCOPE = {"HORIZONTAL":HORIZONTAL,
                    "VERTICAL":VERTICAL,
                    "LEFT":LEFT,
                    "RIGHT":RIGHT,
                    "TOP":TOP,
                    "BOTTOM":BOTTOM,
                    "L2R":L2R,
                    "R2L":R2L,
                    "T2B":T2B,
                    "B2T":B2T}
             
    @classmethod
    def isValidFor(cls, valueText):
        """ Return if this class is valid for the given value text """
        return valueText in cls.GLOBAL_SCOPE
    
    def __init__(self, varName):
        """ Initialize the value token """
        self.varName = varName
        
    def getValue(self, scope):
        """ Return the actual value of the given token """
        return self.GLOBAL_SCOPE[self.varName]