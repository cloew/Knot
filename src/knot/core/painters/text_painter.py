from PySide.QtGui import QLabel

class TextPainter:
    """ Handles creation of the Qt widget for drawing text """
    
    def __init__(self, content):
        """ Initialize the Painter with its internal content """
        self.text = content
        
    def draw(self):
        """ Draw the Text Painter """
        widget = QLabel(self.text)
        widget.resize(widget.sizeHint())
        return widget