from .percent_sizing import PercentSizing
from .pixel_sizing import PixelSizing

from kao_decorators import proxy_for

@proxy_for('sizing', ['handlesDimension', 'applyToWidget', 'resize'])
class Fixed:
    """ Represents a method of sizing a widget to a fixed size """
    
    def __init__(self, size, dimension):
        """ Initialize the Percent Sizing """
        if type(size) == int:
            self.sizing = PixelSizing(size, dimension)
        else:
            self.sizing = PercentSizing(size, dimension)