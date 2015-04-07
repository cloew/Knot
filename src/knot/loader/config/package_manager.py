from .config_factory import PackageConfigFactory

from kao_factory.Source.json_source import JsonSource
from kao_modules import KaoModule

import os

class PackageManager:
    """ Manages the loaded pacakges """
    KNOT_PACKAGE_FILE = 'knot-pkg.json'
    
    def __init__(self):
        """ Initialize the Package Manager """
        self.packageToConfig = {}
        
    def __getitem__(self, package):
        """ Return the config for the given package """
        if package not in self.packageToConfig:
            self.packageToConfig[package] = self.loadPackage(package)
        return self.packageToConfig[package]
        
    def loadPackage(self, package):
        """ Load the given package """
        filename = self.findKnotPackageFilename(package)
        source = JsonSource(filename)
        data = source.data
        packageConfig = PackageConfigFactory.load(data)
        packageConfig.setPackageFilename(filename)
        return packageConfig
    
    def findKnotPackageFilename(self, package):
        """ Return the core Knot package filename """
        module = KaoModule(package)
        packageDirectory = os.path.dirname(module.filename)
        return os.path.join(packageDirectory, self.KNOT_PACKAGE_FILE)
        
PackageManager = PackageManager()