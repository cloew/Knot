from knot import KnotService

class ImageController:
    """ Handle the image to determine the file to load """
    fileLoader = KnotService('fileLoader')
    
    def __init__(self, filename):
        """ Initialize the controller with the image to load """
        self.filename = self.fileLoader.getProperPath(filename)