from .child_token_processor import ChildTokenProcessor
from .token_roles import WIDGET
from .type_token import TypeToken

from knot.exceptions import KnotParseError

from kao_decorators import proxy_for

@proxy_for('processor', ['children', 'attributes', 'content'])
class WidgetToken:
    """ Represents a tokenized widget from a knot file """
    ROLE = WIDGET
    
    @classmethod
    def isValidFor(cls, section):
        """ Return if this token is valid for the given section """
        return section[0].endswith(':')
        
    @staticmethod
    def getWidgetType(section):
        """ Find the widget type in the given section """
        firstLine = section[0]
        return TypeToken(firstLine.split(':')[0])
    
    def __init__(self, section, factory):
        """ Intialize the Widget Token with the section it was loaded from """
        self.widgetType = self.getWidgetType(section)
        self.processor = ChildTokenProcessor(self, factory)
        self.processor.process(section[1:])
        
    def build(self, factory, scope, **kwargs):
        """ Build this type from the factory """
        if not factory.isValidType(self.widgetType.type):
            raise KnotParseError('Unknown widget: {0}'.format(self.widgetType.type))
        
        content = self.content.build(scope) if self.content is not None else None
        widget = factory.build(self.widgetType.type, content, *self.widgetType.getArgumentValues(scope), **kwargs)
        return widget
        
    def getChildConfig(self, config):
        """ Return the config to be used for any child widgets """
        widgetConfig = config.widgetFactory.config[self.widgetType.type]
        if len(widgetConfig.childWidgetConfigs) > 0:
            config = config.copy(additionalWidgetConfigs=widgetConfig.childWidgetConfigs)
        return config
        
    def __repr__(self):
        return "<WidgetToken:{0},{1}, [{2}]>".format(self.widgetType, self.content, ", ".join([repr(child) for child in self.children]))