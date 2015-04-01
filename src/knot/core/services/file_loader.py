from knot import KnotService, use_knot_services

from kao_decorators import proxy_for

import os

@proxy_for('resourceDirectory', ['getProperPath'])
class FileLoader:
    """ Service to allow handling of file paths for the application """
    
    @use_knot_services
    def __init__(self, app=KnotService):
        """ Initialize the Service with the application service """
        self.resourceDirectory = app.resourceDirectory