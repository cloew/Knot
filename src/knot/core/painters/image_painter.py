from .painter import Painter
from knot.policy.default_policies_via_class import DefaultPoliciesViaClass
from knot.core.sizing.use_size_hint import UseSizeHint

from PySide.QtCore import Qt
from PySide.QtGui import QLabel, QPixmap

class ImagePainter(Painter):
    """ Handles creation of the Qt widget for drawing an image """
    DEFAULT_SIZING = DefaultPoliciesViaClass(UseSizeHint)
        
    def buildQWidget(self, widget):
        """ Build the QLabel """
        label = QLabel() 
        label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        return label