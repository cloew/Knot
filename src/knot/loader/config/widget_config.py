from knot.widget.widget import Widget
from kao_modules import NamespacedClass

class WidgetConfig:
    """ Represents the configuration for a widget """
    
    def __init__(self, name, painterClassname, controllerClassname=None):
        """ Initialize the widget config with its name and the painter classname """
        self.name = name
        self.controllerClassname = controllerClassname
        self.painterClassname = painterClassname
        self.namespacedPainterClass = NamespacedClass(self.painterClassname)
        self.namespacedControllerClass = None if controllerClassname is None else NamespacedClass(self.controllerClassname)
        
    def build(self, content, *args, positioning=None, sizing=None, **kwargs):
        """ Return the proper widget object """
        controller = None if self.namespacedControllerClass is None else self.namespacedControllerClass.instantiate(*args, **kwargs)
        painter = self.namespacedPainterClass.instantiate(content, controller)
        return Widget(painter, controller=controller, positioning=positioning, sizing=sizing)
        
    def __repr__(self):
        """ Return the string representation of the config """
        return "<WidgetConfig({0}, {1}, {2})>".format(self.name, self.painterClassname, self.controllerClassname)