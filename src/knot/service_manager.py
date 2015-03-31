
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
        
    def getService(self, name): 
        """ Return the requested service """
        if name not in self.nameToService:
            self.addService(name, self.nameToClass[name])
            
        return self.nameToService[name]
        
ServiceManager = ServiceManager()