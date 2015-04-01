from knot import KnotService, use_knot_services

class ImageController:
    """ Handle the image to determine the file to load """
    
    @use_knot_services
    def __init__(self, filename, fileLoader=KnotService):
        """ Initialize the controller with the image to load """
        self.filename = fileLoader.getProperPath(filename)