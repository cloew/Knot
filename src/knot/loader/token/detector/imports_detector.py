
class ImportsDetector:
    """ Detects section for imports in a Knot file """
    
    def isStart(self, line):
        """ Return if the given line is the start of the Knot imports """
        return line.startswith('import')
        
    def isEnd(self, line):
        """ Returns if the given line is the end of the Knot imports """
        if line.isLastLine():
            return True
        else:
            nextLine = line.next()
            return not nextLine.startswith('import')