
class ContentValue:
    """ Represents a Content Value """
    
    def __init__(self, valueText):
        """ Initialize the value token """
        self.value = valueText
        
    def getValue(self, scope):
        """ Return the actual value of the given token """
        return self.value