from .painter import Painter
from knot.dimensions import HORIZONTAL, VERTICAL, BOTH
from knot.core.sizing.use_size_hint import UseSizeHint

from PySide.QtCore import Qt
from PySide.QtGui import QLabel, QPixmap

class ImagePainter(Painter):
    """ Handles creation of the Qt widget for drawing an image """
    DEFAULT_SIZING = {BOTH:      UseSizeHint(),
                      HORIZONTAL:UseSizeHint(dimension=HORIZONTAL),
                      VERTICAL:  UseSizeHint(dimension=VERTICAL)}
    
    def __init__(self, content):
        """ Initialize the Painter with its internal content """
        Painter.__init__(self)
        
    def buildQWidget(self, widget):
        """ Build the QLabel """
        label = QLabel() 
        label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        label.setPixmap(QPixmap("placeholder.png"))
        return label