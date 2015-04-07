from .config_helper import ConvertConfigsToDictionary

from knot.widget.widget import Widget
from knot.widget.semantic_widget import SemanticWidget

from kao_modules import NamespacedClass
from kao_resources import ResourceDirectory

WIDGET_TYPE = "widget"
SEMANTIC_TYPE = "semantic"

class WidgetConfig:
    """ Represents the configuration for a widget """
    WIDGET_BUILDERS = {WIDGET_TYPE: 'buildWidget',
                       SEMANTIC_TYPE: 'buildSemanticWidget'}
    
    def __init__(self, name, type=WIDGET_TYPE, painterClassname=None, template=None, controllerClassname=None, reqMods=[], childWidgetConfigs=[]):
        """ Initialize the widget config with its name and the painter classname """
        self.name = name
        self.type = type
        self.controllerClassname = controllerClassname
        self.painterClassname = painterClassname
        self.template = template
        self.reqMods = reqMods
        self.childWidgetConfigs = ConvertConfigsToDictionary(childWidgetConfigs)
        
        self.namespacedPainterClass = self.tryToBuildNamespacedClass(painterClassname)
        self.namespacedControllerClass = self.tryToBuildNamespacedClass(controllerClassname)
        
    def setPackageFilename(self, filename):
        """ Set the package filename """
        self.packageDirectory = ResourceDirectory(filename)
        
    def build(self, content, *args, positionings=None, sizings=None, **kwargs):
        """ Return the proper widget object """
        controller = self.tryToIntantiateClass(self.namespacedControllerClass, *args, **kwargs)
        mods = [reqMod.build() for reqMod in self.reqMods]
        
        builder = getattr(self, self.WIDGET_BUILDERS[self.type])
        widget = builder(content, controller, mods, *args, positionings=positionings, sizings=sizings, **kwargs)
        self.tryToLoadChildren(widget)
        return widget
        
    def buildWidget(self, content, controller, mods, *args, positionings=None, sizings=None, **kwargs):
        """ Build the widget object """
        painter = self.tryToIntantiateClass(self.namespacedPainterClass, content, controller)
        return Widget(self.name, content, painter=painter, controller=controller, positionings=positionings, sizings=sizings, mods=mods)
        
    def buildSemanticWidget(self, content, controller, mods, *args, **kwargs):
        """ Build the semantic widget object """
        return SemanticWidget(self.name, content, controller=controller, mods=mods)
        
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