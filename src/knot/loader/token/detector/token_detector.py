from .attribute_detector import AttributeDetector
from .knot_scope_detector import KnotScopeDetector

class TokenDetector:
    """ Detects a section that corresponds to a Knot Token """
    
    def __init__(self):
        """ Initialize the function detector """
        self.detector = None
        self.detectors = [AttributeDetector('position'), KnotScopeDetector()]
    
    def isStart(self, line):
        """ Return if the given line is the start of a Knot Token """
        for detector in self.detectors:
            if detector.isStart(line):
                self.detector = detector
                return True
        else:
            return False
        
    def isEnd(self, line):
        """ Returns if the given line is the end of a Knot Token """
        return self.detector.isEnd(line)