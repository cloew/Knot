from .child_token_processor import ChildTokenProcessor
from .token_roles import WIDGET
from .type_token import TypeToken

class WidgetToken:
    """ Represents a tokenized widget from a knot file """
    ROLE = WIDGET
    
    @classmethod
    def isValidFor(cls, section, config):
        """ Return if this token is valid for the given section """
        widgetType = cls.getWidgetType(section)
        return widgetType is not None and config.widgetFactory.isValidType(widgetType.type)
        
    @staticmethod
    def getWidgetType(section):
        """ Find the widget type in the given section """
        firstLine = section[0]
        return TypeToken(firstLine)
    
    def __init__(self, section, factory):
        """ Intialize the Widget Token with the section it was loaded from """
        self.widgetType = self.getWidgetType(section)
        
        self.children = []
        self.signals = []
        self.attributes = {}
        self.content = None
        self.style = None
        
        processor = ChildTokenProcessor(self, factory)
        processor.process(section[1:])
        self.config = processor.config
        
    def addChild(self, child):
        """ Add the child to the list of tracked child widgets """
        self.children.append(child)
        
    def setContent(self, content):
        """ Set the child content """
        self.content = content
        
    def setStyle(self, style):
        """ Set the style """
        self.style = style
        
    def setSignal(self, signal):
        """ Set the child content """
        self.signals.append(signal)
        
    def setAttribute(self, token):
        """ Set the attribute """
        self.attributes[token.attribute] = token
        
    def build(self, factory, scope, **kwargs):
        """ Build this type form the factory """
        content = self.content.build(scope) if self.content is not None else None
        style = self.style.styling if self.style is not None else None
        widget = factory.build(self.widgetType.type, content, *self.widgetType.getArgumentValues(scope), styling=style, **kwargs)
        
        for signal in self.signals:
            signal.attach(widget.controller, scope)
        return widget
        
    def __repr__(self):
        return "<WidgetToken:{0},{1}, [{2}]>".format(self.widgetType, self.content, ", ".join([repr(child) for child in self.children]))