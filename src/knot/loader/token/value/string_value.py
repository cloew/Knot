
class StringValue:
    """ Represents a String Value """
             
    @classmethod
    def isValidFor(cls, valueText):
        """ Return if this class is valid for the given value text """
        firstCharacter = valueText[0]
        lastCharacter = valueText[-1]
        if firstCharacter in ["'", '"'] and lastCharacter == firstCharacter:
            pieces = valueText.split(firstCharacter)
            allValid = False
            for piece in pieces[1:-2]:
                if piece[-1] != '\\':
                    break
            else:
                allValid = True
            return allValid
        else:
            return False
    
    def __init__(self, valueText):
        """ Initialize the value token """
        self.stringValue = valueText[1:-1]
        
    def getValue(self, scope):
        """ Return the actual value of the given token """
        return self.stringValue