from .package_manager import PackageManager
from ..attributes import POSITION, SIZING
from ..factory.knot_config_factory import KnotConfigFactory

class LoaderConfig:
    """ Represents the configured widgets and attributes available to load """
    CORE_KNOT_PACKAGE = 'knot.core'
    
    def __init__(self):
        """ Initialize the loader config """
        self.widgetFactory = KnotConfigFactory()
        self.attributesFactory = {}
        self.attributesFactory[POSITION] = KnotConfigFactory()
        self.attributesFactory[SIZING] = KnotConfigFactory()
        
        self.importPackage(self.CORE_KNOT_PACKAGE)
        
    def importPackage(self, package):
        """ Import the given package and add its public Knot Entities to the relevant factories """
        packageConfig = PackageManager[package]
        self.widgetFactory.update(packageConfig.widgetConfigs)
        self.attributesFactory[POSITION].update(packageConfig.positioningConfigs)
        self.attributesFactory[SIZING].update(packageConfig.sizingConfigs)