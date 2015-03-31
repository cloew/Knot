from .service_manager import ServiceManager

class ServiceProvider:
    """ Provides the service based on the kwarg name """
        
    def shouldProvide(self, argument, args, kwargs):
        """ Return if the Provider should be used """
        return False
        
    def getValue(self, argument, *args, **kwargs):
        """ Return the value for this default """
        return ServiceManager.getService(argument)