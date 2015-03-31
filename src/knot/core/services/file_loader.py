from knot.service_provider import ServiceProvider
from smart_defaults import smart_defaults

import os

class FileLoader:
    """ Service to allow handling of file paths for the application """
    
    @smart_defaults
    def __init__(self, app=ServiceProvider()):
        """ Initialize the Service with the application service """
        self.root_dir = app.root_dir
        
    def getProperPath(self, filename):
        """ Return the actual path to the application file given """
        return os.path.join(self.root_dir, filename)