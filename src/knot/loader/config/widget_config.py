from .config_helper import ConvertConfigsToDictionary
from .optional_namespaced_class import OptionalNamespacedClass

from knot.widget.widget import Widget
from knot.widget.passthrough_widget import PassthroughWidget
from knot.widget.semantic_widget import SemanticWidget

from kao_modules import NamespacedClass
from kao_resources import ResourceDirectory

WIDGET_TYPE = "widget"
PASSTHROUGH_TYPE = "passthrough"
SEMANTIC_TYPE = "semantic"

class WidgetConfig:
    """ Represents the configuration for a widget """
    WIDGET_BUILDERS = {WIDGET_TYPE: 'buildWidget',
                       PASSTHROUGH_TYPE: 'buildPassthroughWidget',
                       SEMANTIC_TYPE: 'buildSemanticWidget'}
    
    def __init__(self, name, type=WIDGET_TYPE, painterClassname=None, template=None, controllerClassname=None, reqMods=[], childWidgetConfigs=[]):
        """ Initialize the widget config with its name and the painter classname """
        self.name = name
        self.type = type
        self.controllerClass = OptionalNamespacedClass(controllerClassname)
        self.painterClass = OptionalNamespacedClass(painterClassname)
        self.template = template
        self.reqMods = reqMods
        self.childWidgetConfigs = ConvertConfigsToDictionary(childWidgetConfigs)
        
    def setPackageFilename(self, filename):
        """ Set the package filename """
        self.packageDirectory = ResourceDirectory(filename)
        
    def build(self, content, *args, positionings=None, sizings=None, styling=None, **kwargs):
        """ Return the proper widget object """
        controller = self.controllerClass.tryToIntantiateClass(*args, **kwargs)
        mods = [reqMod.build() for reqMod in self.reqMods]
        
        builder = getattr(self, self.WIDGET_BUILDERS[self.type])
        widget = builder(content, controller, mods, *args, positionings=positionings, sizings=sizings, styling=styling, **kwargs)
        self.tryToLoadChildren(widget)
        return widget
        
    def buildWidget(self, content, controller, mods, *args, positionings=None, sizings=None, styling=None, **kwargs):
        """ Build the widget object """
        painter = self.painterClass.tryToIntantiateClass(content)
        return Widget(self.name, content, painter=painter, controller=controller, positionings=positionings, sizings=sizings, mods=mods, styling=styling)
        
    def buildPassthroughWidget(self, content, controller, mods, *args, **kwargs):
        """ Build the passthrough widget object """
        return PassthroughWidget(self.name, content, controller=controller, mods=mods)
        
    def buildSemanticWidget(self, content, controller, mods, *args, **kwargs):
        """ Build the semantic widget object """
        return SemanticWidget(self.name, content, controller=controller, mods=mods)
        
    def tryToLoadChildren(self, widget):
        """ Load children for this widget based on its configuration """
        if self.template is None:
            return
            
        from ..knot_loader import KnotLoader
        knotLoader = KnotLoader(self.packageDirectory.getProperPath(self.template))
        knotLoader.load(onto=widget)
        
    def __repr__(self):
        """ Return the string representation of the config """
        return "<WidgetConfig({0}, {1}, {2})>".format(self.name, self.painterClassname, self.controllerClassname)