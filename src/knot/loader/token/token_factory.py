from .attribute_token import AttributeToken
from .content_token import ContentToken
from .import_token import ImportToken
from .signal_token import SignalToken
from .widget_token import WidgetToken

from .detector.token_detector import TokenDetector

from kao_file import KaoFile, SectionFinder

class TokenFactory:
    """ Represents a tokenized widget from a knot file """
    
    def __init__(self, config):
        """ Initialize the loader with the configuration to use """
        self.config = config
        
    def loadImportTokens(self, lines):
        """ Load the import tokens """
        return [ImportToken(line) for line in lines if ImportToken.isValidFor(line)]
    
    def loadAllTokens(self, lines):
        """ Load and return all Widget Tokens at the same depth from the given lines """
        file = KaoFile(lines)
        sectionFinder = SectionFinder(TokenDetector())
        section = None
        nextSectionStartsOn = 0
        
        tokens = []
        
        while True:
            section = sectionFinder.find(file, startAt=nextSectionStartsOn)
            if section is None:
                break
            else:
                tokens.append(self.load(section))
                if file.getLineAt(section.endIndex).isLastLine():
                    break
                else:
                    nextSectionStartsOn = file.getLineAt(section.endIndex).next().lineIndex
                
        return tokens
    
    def load(self, section):
        """ Load a token from the given section """
        if WidgetToken.isValidFor(section, self.config):
            return WidgetToken(section, self)
        else:
            for tokenCls in [SignalToken, AttributeToken, ContentToken]:
                if tokenCls.isValidFor(section):
                    return tokenCls(section)