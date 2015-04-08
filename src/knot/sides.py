from .dimensions import HORIZONTAL, VERTICAL

class Side:
    """ Represents a side of the widget """
    
    def __init__(self, name, dimension):
        """ The dimension this side is a part of """
        self.name = name
        self.dimension = dimension
        
    def __repr__(self):
        return "<Side: {0}>".format(self.name)

LEFT = Side("Left", HORIZONTAL)
RIGHT = Side("Right", HORIZONTAL)
TOP = Side("Top", VERTICAL)
BOTTOM = Side("Bottom", VERTICAL)

LEFT.oppositeSide = RIGHT
RIGHT.oppositeSide = LEFT
TOP.oppositeSide = BOTTOM
BOTTOM.oppositeSide = TOP