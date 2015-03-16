from PySide.QtGui import QLabel

class TextPainter:
    """ Handles creation of the Qt widget for drawing text """
    
    def __init__(self, content):
        """ Initialize the Painter with its internal content """
        self.text = content
        
    def draw(self, widget):
        """ Draw the Text Painter """
        qwidget = QLabel(self.text)
        qwidget.resize(qwidget.sizeHint())
        return qwidget