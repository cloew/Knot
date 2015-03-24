from .dimensions import HORIZONTAL, VERTICAL
class Side:
    """ Represents a side of the widget """
    
    def __init__(self, dimension):
        """ The dimension this side is a part of """
        self.dimension = dimension

LEFT = Side(HORIZONTAL)
RIGHT = Side(HORIZONTAL)
TOP = Side(VERTICAL)
BOTTOM = Side(VERTICAL)