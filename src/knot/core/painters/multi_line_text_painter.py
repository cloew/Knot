from .painter import Painter
from knot.dimensions import HORIZONTAL, VERTICAL, BOTH
from knot.core.sizing.stretch import Stretch
from knot.core.sizing.use_size_hint import UseSizeHint

from PySide.QtCore import Qt
from PySide.QtGui import QLabel

class MultiLineTextPainter(Painter):
    """ Handles creation of the Qt widget for drawing multi-line text """
    DEFAULT_SIZING = {BOTH:     [Stretch(dimension=HORIZONTAL), UseSizeHint(dimension=VERTICAL)],
                      HORIZONTAL:Stretch(dimension=HORIZONTAL),
                      VERTICAL:  UseSizeHint(dimension=VERTICAL)}
    
    def __init__(self, content):
        """ Initialize the Painter with its internal content """
        Painter.__init__(self)
        self.text = content
        
    def buildQWidget(self, widget):
        """ Build the QLabel """
        label = QLabel(self.text) 
        label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        label.setWordWrap(True)
        return label