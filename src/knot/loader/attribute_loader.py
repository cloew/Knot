from .factory.positioning_factory import PositioningFactory

class AttributeLoader:
    """ Helper class to load attributes from knot tokens """
    
    def load(self, attrToken):
        """ Load the given attribute token """
        positionType = attrToken.value
        return PositioningFactory.build(positionType)