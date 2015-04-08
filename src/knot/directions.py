from .dimensions import HORIZONTAL, VERTICAL
from .sides import LEFT, RIGHT, TOP, BOTTOM

class Direction:
    """ Represents a direction """
    
    def __init__(self, dimension, startingSide):
        """ Initialize the direction with the dimension its in and the side to start from """
        self.dimension = dimension
        self.startingSide = startingSide
        
L2R = Direction(HORIZONTAL, LEFT)
R2L = Direction(HORIZONTAL, RIGHT)
T2B = Direction(VERTICAL, TOP)
B2T = Direction(VERTICAL, BOTTOM)