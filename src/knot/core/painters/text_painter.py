from .painter import Painter

from PySide.QtGui import QLabel

class TextPainter(Painter):
    """ Handles creation of the Qt widget for drawing text """
    
    def __init__(self, content):
        """ Initialize the Painter with its internal content """
        Painter.__init__(self)
        self.text = content
        
    def buildQWidget(self, widget):
        """ Build the QLabel """
        return QLabel(self.text)