from .painter import Painter
from knot.dimensions import HORIZONTAL, VERTICAL, BOTH
from knot.core.sizing.use_size_hint import UseSizeHint

from PySide.QtCore import Qt
from PySide.QtGui import QPushButton

class ButtonPainter(Painter):
    """ Handles creation of the Qt widget for drawing a button """
    DEFAULT_SIZING = {BOTH:      UseSizeHint(),
                      HORIZONTAL:UseSizeHint(dimension=HORIZONTAL),
                      VERTICAL:  UseSizeHint(dimension=VERTICAL)}
    
    def __init__(self, content):
        """ Initialize the Painter with its internal content """
        Painter.__init__(self)
        self.text = content
        
    def buildQWidget(self, widget):
        """ Build the QPushButton """
        button = QPushButton(self.text)
        return button