from knot import KnotService
from knot.events.event_types import WIDGET_CREATED

from PySide.QtGui import QPixmap

class ImageController:
    """ Handle the image to determine the file to load """
    fileLoader = KnotService('fileLoader')
    
    def __init__(self, filename):
        """ Initialize the controller with the image to load """
        self.filename = self.fileLoader.getProperPath(filename)
        
    def attachWidget(self, widget):
        """ Attach the widget """
        self.widget = widget
        widget.on(WIDGET_CREATED, self.setImage)
        
    def setImage(self, widget=None, event=None):
        """ Set the image for the underlying qt widget """
        pixmap = QPixmap(self.filename)
        self.widget._qwidget.setPixmap(pixmap)