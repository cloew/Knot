from .painter import Painter
from knot.policy.default_policies_via_class import DefaultPoliciesViaClass
from knot.core.sizing.use_size_hint import UseSizeHint

from PySide.QtCore import Qt
from PySide.QtGui import QLabel, QPixmap

class ImagePainter(Painter):
    """ Handles creation of the Qt widget for drawing an image """
    DEFAULT_SIZING = DefaultPoliciesViaClass(UseSizeHint)
    
    def __init__(self, content, controller):
        """ Initialize the Painter with its internal content """
        Painter.__init__(self)
        self.filename = controller.filename
        
    def buildQWidget(self, widget):
        """ Build the QLabel """
        label = QLabel() 
        label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        label.setPixmap(QPixmap(self.filename))
        return label