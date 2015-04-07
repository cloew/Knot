
def LoopUntilCharMatches(text, match, specialCharacters):
    """ Loop until a matching character is found """
    i = 0
    while i < len(text):
        c = text[i]
        if c in specialCharacters:
            i += specialCharacters[c].findEnd(text[i+1:], specialCharacters)
        elif c == match:
            return i
        i += 1
    return None

class KnotSpecialCharacter:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        
    def findEnd(self, text, specialCharacters):
        """ Return the matching end of this special character """
        i = LoopUntilCharMatches(text, self.stop, specialCharacters)
        if i is None:
            i = len(text)
            # Throw an unmatched char exception..?
        return i
        

class KnotListParser:
    """ Helper class to parse lists in knot files """
    specialCharacters = {specialChar.start:specialChar for specialChar in [KnotSpecialCharacter('(', ')')]}
    
    def parse(self, text):
        """ Return the list of strings separated from the Knot list """
        text = text.strip()
        pieces = []
        
        start = 0
        while start < len(text):
            end = self.findPieceEnd(text[start:])
            pieces.append(text[start:start+end])
            start += (end + 1)
            
        return pieces
        
    def findPieceEnd(self, text):
        i = LoopUntilCharMatches(text, ',', self.specialCharacters)
        if i is None:
            i = len(text)
        return i