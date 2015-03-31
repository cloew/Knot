
class ServiceManager:
    """ Manages all the available services """
    
    def __init__(self):
        """ Initialize the Service Manager """
        self.nameToClass = {}
        self.nameToService = {}
        
    def addService(self, name, service):
        """ Add the given service """
        self.nameToService[name] = service
        
    def registerService(self, name, serviceCls):
        """ Register the given service class """
        self.nameToClass[name] = serviceCls
        
ServiceManager = ServiceManager()