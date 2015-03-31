from .painter import Painter
from knot.dimensions import HORIZONTAL, VERTICAL, BOTH
from knot.core.sizing.use_size_hint import UseSizeHint

from PySide.QtCore import Qt
from PySide.QtGui import QLabel

class TextPainter(Painter):
    """ Handles creation of the Qt widget for drawing text """
    DEFAULT_SIZING = {BOTH:      UseSizeHint(),
                      HORIZONTAL:UseSizeHint(dimension=HORIZONTAL),
                      VERTICAL:  UseSizeHint(dimension=VERTICAL)}
    
    def __init__(self, content, controller=None):
        """ Initialize the Painter with its internal content """
        Painter.__init__(self)
        self.text = content
        
    def buildQWidget(self, widget):
        """ Build the QLabel """
        label = QLabel(self.text) 
        label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        return label