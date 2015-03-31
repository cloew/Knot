from knot.service_manager import ServiceManager
from kao_modules import NamespacedClass

class ServiceConfig:
    """ Represents the configuration for a policy """
    
    def __init__(self, name, serviceClassname):
        """ Initialize the service config with its name and the service classname """
        self.name = name
        self.serviceClassname = serviceClassname
        self.namespacedClass = NamespacedClass(self.serviceClassname)
        
        ServiceManager.registerService(name, self.namespacedClass.cls)
        
    def __repr__(self):
        """ Return the string representation of the config """
        return "<ServiceConfig({0}, {1})>".format(self.name, self.serviceClassname)