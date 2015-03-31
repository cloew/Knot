from knot.service_provider import ServiceProvider
from smart_defaults import smart_defaults

class ImageController:
    """ Handle the image to determine the file to load """
    
    @smart_defaults
    def __init__(self, filename, fileLoader=ServiceProvider()):
        """ Initialize the controller with the image to load """
        self.filename = fileLoader.getProperPath(filename)