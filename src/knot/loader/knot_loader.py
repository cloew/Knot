from .import_loader import ImportLoader
from .widget_loader import WidgetLoader
from .scope_getter import GetScopeFor
from .config.loader_config import LoaderConfig

from .token.token_factory import TokenFactory
from .token.token_roles import IMPORT, WIDGET
from .token.detector.imports_detector import ImportsDetector

from kao_file import KaoFile, SectionFinder

class KnotLoader:
    """ Loads Knot files and converts them to the proper widget tree """
    
    def __init__(self, filename):
        """ Initialize with the file to load from """
        self.filename = filename
        self.file = KaoFile.open(self.filename)
        self.config = LoaderConfig()
        self.factory = TokenFactory()
        
    def loadOnto(self, widget):
        """ Load the contents of the given file and place them on the given widget """
        children = self.load(scope=GetScopeFor(widget))
        for child in children:
            widget.addChild(child)
        
    def load(self, scope=None):
        """ Load the widgets from the filename """
        self.findSections()
        self.loadImports()
        return self.loadWidgets(scope=scope)
        
    def findSections(self):
        """ Find the imports and widgets sections of the Knot File """
        file = KaoFile.open(self.filename)
        sectionFinder = SectionFinder(ImportsDetector())
        importsSection = sectionFinder.find(file)
        if importsSection is not None:
            self.importsLines = importsSection.lines
            self.widgetsLines = file.lines[importsSection.endIndex+1:]
        else:
            self.importsLines = []
            self.widgetsLines = file.lines
        
    def loadImports(self):
        """ Load the widget section of the Knot File """
        tokens = self.factory.loadImportTokens(self.importsLines)
        importLoader = ImportLoader(self.config)
        return [importLoader.load(token) for token in tokens if token.ROLE is IMPORT]
        
    def loadWidgets(self, scope=None):
        """ Load the widget section of the Knot File """
        tokens = self.factory.loadAllTokens(self.widgetsLines)
        widgetLoader = WidgetLoader(self.config)
        return [widgetLoader.load(token, scope=scope) for token in tokens if token.ROLE is WIDGET]