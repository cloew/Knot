from .token.token_factory import TokenFactory
from .token.detector.imports_detector import ImportsDetector
from kao_file import KaoFile, SectionFinder

class Tokenizer:
    """ Helper to tokenize the given text """
    
    def __init__(self, filename):
        """ Initialize with the filename to tokenize """
        self.file = KaoFile.open(filename)
        self.factory = TokenFactory()
        
    def tokenize(self):
        """ Return the import and component tokens for the file """
        self.findSections()
        return self.loadImports(), self.loadComponents()
        
    def findSections(self):
        """ Find the imports and widgets sections of the Knot File """
        sectionFinder = SectionFinder(ImportsDetector())
        importsSection = sectionFinder.find(self.file)
        if importsSection is not None:
            self.importsLines = importsSection.lines
            self.widgetsLines = self.file.lines[importsSection.endIndex+1:]
        else:
            self.importsLines = []
            self.widgetsLines = self.file.lines
        
    def loadImports(self):
        """ Load the widget section of the Knot File """
        return self.factory.loadImportTokens(self.importsLines)
        
    def loadComponents(self):
        """ Load the widget section of the Knot File """
        return self.factory.loadAllTokens(self.widgetsLines)
        