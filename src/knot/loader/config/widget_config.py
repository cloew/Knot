from .config_helper import ConvertConfigsToDictionary
from .optional_namespaced_class import OptionalNamespacedClass
from .widget import builder_factory
from ..knot_loader import KnotLoader

from kao_resources import ResourceDirectory

class WidgetConfig:
    """ Represents the configuration for a widget """
    
    def __init__(self, name, type=builder_factory.WIDGET_TYPE, painterClassname=None, template=None, controllerClassname=None, reqMods=[], childWidgetConfigs=[]):
        """ Initialize the widget config with its name and the painter classname """
        self.name = name
        self.type = type
        self.builder = builder_factory.getBuilder(type, name, painterClassname)
        self.controllerClass = OptionalNamespacedClass(controllerClassname)
        self.template = template
        self.reqMods = reqMods
        self.childWidgetConfigs = ConvertConfigsToDictionary(childWidgetConfigs)
        
    def setPackageFilename(self, filename):
        """ Set the package filename """
        self.packageDirectory = ResourceDirectory(filename)
        
    def build(self, token, content, *args, positionings=None, sizings=None, styling=None, **kwargs):
        """ Return the proper widget object """
        controller = self.controllerClass.tryToIntantiateClass(*args, **kwargs)
        mods = [reqMod.build() for reqMod in self.reqMods]
        widget = self.builder.build(content, controller, mods, *args, positionings=positionings, sizings=sizings, styling=styling, **kwargs)
        self.tryToLoadChildren(widget, token)
        return widget
        
    def tryToLoadChildren(self, widget, token):
        """ Load children for this widget based on its configuration """
        if self.template is None:
            return
            
        from .loader_config import LoaderConfig
        config = LoaderConfig()
        if token.parent is not None and self.type == builder_factory.PASSTHROUGH_TYPE:
            config = config.copy(additionalWidgetConfigs=token.parent.config.childWidgetConfigs)
        knotLoader = KnotLoader(self.packageDirectory.getProperPath(self.template), config)
        knotLoader.load(onto=widget)
        
    def __repr__(self):
        """ Return the string representation of the config """
        return "<WidgetConfig({0})>".format(self.name)