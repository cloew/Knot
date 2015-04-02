from knot.dimensions import HORIZONTAL, VERTICAL, BOTH
from knot.policy.default_policies_via_class import DefaultPoliciesViaClass
from knot.core.painters.painter import Painter
from knot.core.sizing.use_size_hint import UseSizeHint

from PySide.QtGui import QPushButton

class ButtonPainter(Painter):
    """ Handles creation of the Qt widget for drawing a button """
    DEFAULT_SIZING = DefaultPoliciesViaClass(UseSizeHint)
    
    def __init__(self, content, controller=None):
        """ Initialize the Painter with its internal content """
        Painter.__init__(self)
        self.content = content
        
    def buildQWidget(self, widget):
        """ Build the QPushButton """
        button = QPushButton(self.content.text)
        return button