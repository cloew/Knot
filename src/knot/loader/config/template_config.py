from .widget.builder_factory import PASSTHROUGH_TYPE
from ..knot_loader import KnotLoader

from kao_resources import ResourceDirectory

class TemplateConfig:
    """ Represents the configuration for a template to be used for a widget """
    
    def __init__(self, type, template):
        """ Initialize the config with the template filename """
        self.type = type
        self.template = template
        
    def setPackageFilename(self, filename):
        """ Set the package filename """
        self.packageDirectory = ResourceDirectory(filename)
        
    def load(self, widget, token):
        """ Load children for this widget from the template """
        if self.template is None:
            return
            
        knotLoader = KnotLoader(self.packageDirectory.getProperPath(self.template), self.getConfig(token))
        knotLoader.load(onto=widget)
        
    def getConfig(self, token):
        """ Return the config to use for processing the template """
        from .loader_config import LoaderConfig
        config = LoaderConfig()
        if token.parent is not None and self.type == PASSTHROUGH_TYPE:
            config = config.copy(additionalWidgetConfigs=token.parent.config.childWidgetConfigs)
        return config