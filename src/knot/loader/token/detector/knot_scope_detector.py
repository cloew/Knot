from pyfiles import LeadingWhitespace
    
class KnotScopeDetector:
    """ Detects the section of a knot file defining a new scope """
    
    def __init__(self, startingLine=None):
        """ Initialize the Scope detector """
        self.startingLine = startingLine
    
    def isStart(self, line):
        """ Return if the given line is the start of a Knot Scope """
        isStart = line.strip() != ''
        if isStart:
            self.startingLine = line
        return isStart
        
    def isEnd(self, line):
        """ Returns if the given line is the end of a Knot Scope """
        if line.isLastLine():
            return True
        else:
            nextLine = line.next()
            hasText = not (nextLine.strip() == '')
            lessWhitespace = LeadingWhitespace(line.next()) <= LeadingWhitespace(self.startingLine)
            return hasText and lessWhitespace