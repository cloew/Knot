from .widget_loader import WidgetLoader
from .token.token_factory import TokenFactory
from .token.token_roles import WIDGET
from kao_file import KaoFile

class KnotLoader:
    """ Loads Knot files and converts them to the proper widget tree """
    
    def __init__(self, filename):
        """ Initialize with the file to load from """
        self.filename = filename
        
    def load(self):
        """ Load the widgets from the filename """
        tokens = self.getTokens()
        return self.loadWidgets(tokens)
        
    def getTokens(self):
        """ Return the widget token tree """
        factory = TokenFactory()
        file = KaoFile.open(self.filename)
        return factory.loadAllTokens(file.lines)
        
    def loadWidgets(self, tokens):
        """ Load the widgets from the given tokens """
        widgetLoader = WidgetLoader()
        return [widgetLoader.load(token) for token in tokens if token.ROLE is WIDGET]