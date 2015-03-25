from .config_factory import PackageConfigFactory
from ..attributes import POSITION, SIZING
from ..factory.knot_config_factory import KnotConfigFactory

from kao_factory.Source.json_source import JsonSource
from kao_modules import KaoModule

import os

class LoaderConfig:
    """ Represents the configured widgets and attributes available to load """
    CORE_KNOT_PACKAGE = 'knot.core'
    KNOT_PACKAGE_FILE = 'knot-pkg.json'
    
    def __init__(self):
        """ Initialize the loader config """
        self.packageConfig = self.loadPackage(self.CORE_KNOT_PACKAGE)
        
        self.widgetFactory = KnotConfigFactory(self.packageConfig.widgetConfigs)
        self.attributesFactory = {}
        self.attributesFactory[POSITION] = KnotConfigFactory(self.packageConfig.positioningConfigs)
        self.attributesFactory[SIZING] = KnotConfigFactory(self.packageConfig.sizingConfigs)
        
    def loadPackage(self, package):
        """ Load the given package """
        filename = self.findKnotPackageFilename(package)
        source = JsonSource(filename)
        data = source.data
        return PackageConfigFactory.load(data)
    
    def findKnotPackageFilename(self, package):
        """ Return the core Knot package filename """
        module = KaoModule(package)
        packageDirectory = os.path.dirname(module.filename)
        return os.path.join(packageDirectory, self.KNOT_PACKAGE_FILE)