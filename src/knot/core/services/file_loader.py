from knot.service_provider import ServiceProvider

from kao_decorators import proxy_for
from smart_defaults import smart_defaults

import os

@proxy_for('resourceDirectory', ['getProperPath'])
class FileLoader:
    """ Service to allow handling of file paths for the application """
    
    @smart_defaults
    def __init__(self, app=ServiceProvider()):
        """ Initialize the Service with the application service """
        self.resourceDirectory = app.resourceDirectory