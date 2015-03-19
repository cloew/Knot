from .attribute_token import AttributeToken
from .content_token import ContentToken
from .widget_token import WidgetToken

from .detector.token_detector import TokenDetector
from .parser.widget_type_parser import WidgetTypeParser

from kao_file import KaoFile, SectionFinder

class TokenFactory:
    """ Represents a tokenized widget from a knot file """
    
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
        if WidgetToken.isValidFor(section):
            return WidgetToken(section, self)
        else:
            for tokenCls in [AttributeToken, ContentToken]:
                if tokenCls.isValidFor(section):
                    return tokenCls(section)
        
    def isWidget(self, section):
        """ Return if the given section if for a Widget """
        widgetType = WidgetTypeParser().find(section)
        return widgetType is not None and WidgetFactory.isValidType(widgetType)