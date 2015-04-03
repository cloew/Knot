from knot.widget.widget import Widget

from kao_modules import NamespacedClass
from kao_resources import ResourceDirectory

class WidgetConfig:
    """ Represents the configuration for a widget """
    
    def __init__(self, name, painterClassname=None, template=None, controllerClassname=None, reqMods=[]):
        """ Initialize the widget config with its name and the painter classname """
        self.name = name
        self.controllerClassname = controllerClassname
        self.painterClassname = painterClassname
        self.template = template
        self.reqMods = reqMods
        
        self.namespacedPainterClass = self.tryToBuildNamespacedClass(painterClassname)
        self.namespacedControllerClass = self.tryToBuildNamespacedClass(controllerClassname)
        
    def setPackageFilename(self, filename):
        """ Set the package filename """
        self.packageDirectory = ResourceDirectory(filename)
        
    def build(self, content, *args, positioning=None, sizing=None, **kwargs):
        """ Return the proper widget object """
        controller = self.tryToIntantiateClass(self.namespacedControllerClass, *args, **kwargs)
        painter = self.tryToIntantiateClass(self.namespacedPainterClass, content, controller)
        mods = [reqMod.build() for reqMod in self.reqMods]
        
        widget = Widget(painter, controller=controller, positioning=positioning, sizing=sizing, mods=mods)
        self.tryToLoadChildren(widget)
        return widget
        
    def tryToLoadChildren(self, widget):
        """ Load children for this widget based on its configuration """
        if self.template is None:
            return
            
        from ..knot_loader import KnotLoader
        knotLoader = KnotLoader(self.packageDirectory.getProperPath(self.template))
        knotLoader.loadOnto(widget)
        
    def __repr__(self):
        """ Return the string representation of the config """
        return "<WidgetConfig({0}, {1}, {2})>".format(self.name, self.painterClassname, self.controllerClassname)
        
    def tryToBuildNamespacedClass(self, classname):
        """ Build the Namespaced Class object for the given name if the name is not None """
        return None if classname is None else NamespacedClass(classname)
        
    def tryToIntantiateClass(self, namespacedClass, *args, **kwargs):
        """ Instantiate the Namespaced Class object for the given name if the name is not None """
        return None if namespacedClass is None else namespacedClass.instantiate(*args, **kwargs)