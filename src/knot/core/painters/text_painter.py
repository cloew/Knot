from .painter import Painter
from knot.policy.default_policies_via_class import DefaultPoliciesViaClass
from knot.core.sizing.use_size_hint import UseSizeHint

from PySide.QtCore import Qt
from PySide.QtGui import QLabel

class TextPainter(Painter):
    """ Handles creation of the Qt widget for drawing text """
    DEFAULT_SIZING = DefaultPoliciesViaClass(UseSizeHint)
    
    def __init__(self, content, controller=None):
        """ Initialize the Painter with its internal content """
        Painter.__init__(self)
        self.content = content
        
    def buildQWidget(self, widget):
        """ Build the QLabel """
        label = QLabel(self.content.text) 
        label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        return label