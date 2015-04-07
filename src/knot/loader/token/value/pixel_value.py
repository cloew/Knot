
class PixelValue:
    """ Represents a tokenized pixel value """
             
    @classmethod
    def isValidFor(cls, valueText):
        """ Return if this class is valid for the given value text """
        return valueText.endswith('px')
    
    def __init__(self, value):
        """ Initialize the value token """
        self.value = int(value[:-2])
        
    def getValue(self, scope):
        """ Return the actual value of the given token """
        return self.value