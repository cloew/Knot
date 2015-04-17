from knot.policy.default_policies_via_class import DefaultPoliciesViaClass
from knot.core.painters.painter import Painter
from knot.core.sizing.use_size_hint import UseSizeHint

from PySide.QtGui import QTabWidget 

class TabPainter(Painter):
    """ Handles creation of the Qt widget for drawing a collection of tabs """
    DEFAULT_SIZING = DefaultPoliciesViaClass(UseSizeHint)
        
    def buildQWidget(self, widget):
        """ Build the QTabWidegt """
        return QTabWidget()