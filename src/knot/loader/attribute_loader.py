from .attributes import POSITION, SIZING

from .factory.positioning_factory import PositioningFactory
from .factory.sizing_factory import SizingFactory

class AttributeLoader:
    """ Helper class to load attributes from knot tokens """
    ATTR_TO_FACTORY = {POSITION:PositioningFactory,
                       SIZING:SizingFactory}
    
    def load(self, attribute, attrToken):
        """ Load the given attribute token """
        factory = self.ATTR_TO_FACTORY[attribute]
        return attrToken.type.build(factory)