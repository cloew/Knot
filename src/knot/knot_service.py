from .service_manager import ServiceManager

class KnotService:
    """ Descriptor for a Knot Service """
    
    def __init__(self, serviceName):
        """ Initialize the service with the service name """
        self.serviceName = serviceName
        
    def __get__(self, obj, objtype=None):
        """ Return the service """
        return ServiceManager.getService(self.serviceName)