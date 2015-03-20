from .knot_config_factory import KnotConfigFactory

from knot.widget import Widget

from knot.core.sizing.use_size_hint import UseSizeHint
from knot.core.sizing.shrink_to_contents import ShrinkToContents
from knot.core.sizing.stretch import Stretch

sizings = {'shrink':UseSizeHint,
           'shrink-to-contents':ShrinkToContents,
           'stretch':Stretch}
           
def BuildSizing(sizingType):
    """ Build the Sizing based on its given type """
    sizingCls = sizings[sizingType]
    return sizingCls()
    
SizingFactory = KnotConfigFactory(sizings, BuildSizing)