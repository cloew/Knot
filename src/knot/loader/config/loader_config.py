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
        self.widgetFactory = KnotConfigFactory()
        self.attributesFactory = {}
        self.attributesFactory[POSITION] = KnotConfigFactory()
        self.attributesFactory[SIZING] = KnotConfigFactory()
        
        self.importPackage(self.CORE_KNOT_PACKAGE)
        
    def importPackage(self, package):
        """ Import the given package and add its public Knot Entities to the relevant factories """
        packageConfig = self.loadPackage(package)
        self.widgetFactory.update(packageConfig.widgetConfigs)
        self.attributesFactory[POSITION].update(packageConfig.positioningConfigs)
        self.attributesFactory[SIZING].update(packageConfig.sizingConfigs)
        
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