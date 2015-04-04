from knot import KnotService

from kao_decorators import proxy_for

@proxy_for('resourceDirectory', ['getProperPath'])
class FileLoader:
    """ Service to allow handling of file paths for the application """
    app = KnotService('app')
    
    def __init__(self):
        """ Initialize the Service with the application service """
        self.resourceDirectory = self.app.resourceDirectory