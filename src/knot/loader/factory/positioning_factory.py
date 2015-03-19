from .knot_config_factory import KnotConfigFactory

from knot.widget import Widget

from knot.core.positioning.center import Center
from knot.core.positioning.from_neighbor import FromNeighbor

positionings = {'center':Center,
                'from-neighbor':FromNeighbor}

def BuildPositioning(positioningType):
    """ Build the Positioning based on its given type """
    positioningCls = positionings[positioningType]
    return positioningCls()
    
PositioningFactory = KnotConfigFactory(positionings, BuildPositioning)