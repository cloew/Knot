from knot.widget.widget import Widget
from kao_modules import NamespacedClass

class WidgetConfig:
    """ Represents the configuration for a widget """
    
    def __init__(self, name, painterClassname=None, controllerClassname=None):
        """ Initialize the widget config with its name and the painter classname """
        self.name = name
        self.controllerClassname = controllerClassname
        self.painterClassname = painterClassname
        
        self.namespacedPainterClass = self.tryToBuildNamespacedClass(painterClassname)
        self.namespacedControllerClass = self.tryToBuildNamespacedClass(controllerClassname)
        
    def build(self, content, *args, positioning=None, sizing=None, **kwargs):
        """ Return the proper widget object """
        controller = self.tryToIntantiateClass(self.namespacedControllerClass, *args, **kwargs)
        painter = self.tryToIntantiateClass(self.namespacedPainterClass, content, controller)
        return Widget(painter, controller=controller, positioning=positioning, sizing=sizing)
        
    def __repr__(self):
        """ Return the string representation of the config """
        return "<WidgetConfig({0}, {1}, {2})>".format(self.name, self.painterClassname, self.controllerClassname)
        
    def tryToBuildNamespacedClass(self, classname):
        """ Build the Namespaced Class object for the given name if the name is not None """
        return None if classname is None else NamespacedClass(classname)
        
    def tryToIntantiateClass(self, namespacedClass, *args, **kwargs):
        """ Instantiate the Namespaced Class object for the given name if the name is not None """
        return None if namespacedClass is None else namespacedClass.instantiate(*args, **kwargs)