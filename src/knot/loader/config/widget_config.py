from knot.widget.widget import Widget
from kao_modules import NamespacedClass

class WidgetConfig:
    """ Represents the configuration for a widget """
    
    def __init__(self, name, painterClassname):
        """ Initialize the widget config with its name and the painter classname """
        self.name = name
        self.painterClassname = painterClassname
        self.namespacedPainterClass = NamespacedClass(self.painterClassname)
        
    def build(self, content, positioning=None, sizing=None):
        """ Return the proper widget object """
        painter = self.namespacedPainterClass.instantiate(content)
        return Widget(painter, positioning=positioning, sizing=sizing)
        
    def __repr__(self):
        """ Return the string representation of the config """
        return "<WidgetConfig({0}, {1})>".format(self.name, self.painterClassname)