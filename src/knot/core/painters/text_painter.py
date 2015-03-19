from .painter import Painter
from knot.core.sizing.use_size_hint import UseSizeHint

from PySide.QtCore import Qt
from PySide.QtGui import QLabel

class TextPainter(Painter):
    """ Handles creation of the Qt widget for drawing text """
    DEFAULT_SIZING_CLS = UseSizeHint
    
    def __init__(self, content):
        """ Initialize the Painter with its internal content """
        Painter.__init__(self)
        self.text = content
        
    def buildQWidget(self, widget):
        """ Build the QLabel """
        label = QLabel(self.text) 
        label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        return label