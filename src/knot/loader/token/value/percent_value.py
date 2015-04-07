from decimal import Decimal

class PercentValue:
    """ Represents a tokenized percentage value """
             
    @classmethod
    def isValidFor(cls, valueText):
        """ Return if this class is valid for the given value text """
        return valueText.endswith('%')
    
    def __init__(self, percentage):
        """ Initialize the value token """
        self.percentage = Decimal(percentage[:-1])/100
        
    def getValue(self, scope):
        """ Return the actual value of the given token """
        return self.percentage