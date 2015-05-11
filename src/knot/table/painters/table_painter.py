from knot.policy.default_policies_via_class import DefaultPoliciesViaClass
from knot.core.painters.painter import Painter
from knot.core.sizing.use_size_hint import UseSizeHint

from PySide.QtGui import QTableView  

class TablePainter(Painter):
    """ Handles creation of the Qt widget for drawing a table """
    DEFAULT_SIZING = DefaultPoliciesViaClass(UseSizeHint)
        
    def buildQWidget(self, widget):
        """ Build the QTableView """
        return QTableView()