
class AttributeDetector:
    """ Detects section for a specific attribute """
    
    def __init__(self, attribute):
        """ Initialize the attribute detector with the attribute to detect """
        self.attribute = attribute
    
    def isStart(self, line):
        """ Return if the given line is the start of a Knot Attribute declaration """
        return self.startsWithAttribute(line)
        
    def isEnd(self, line):
        """ Returns if the given line is the end of a Knot Attribute declaration """
        return self.startsWithAttribute(line)
            
    def startsWithAttribute(self, line):
        """ Return if this line starts with an attribute """
        return line.startswith('@{0}'.format(self.attribute))