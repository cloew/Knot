from knot import KnotService, OneWayBinding, apply_knot_bindings
from knot.events.event_types import WIDGET_CREATED

from PySide.QtGui import QPixmap

import os

class ImageController:
    """ Handle the image to determine the file to load """
    app = KnotService('app')
    fileLoader = KnotService('fileLoader')
    _filename = OneWayBinding('_filename')
    
    @apply_knot_bindings
    def __init__(self, _filename):
        """ Initialize the controller with the image to load """
        
    def attachWidget(self, widget):
        """ Attach the widget """
        self.widget = widget
        widget.on(WIDGET_CREATED, self.setImage)
        self.app.watch(self, '_filename', self.setImage)
        
    def setImage(self, widget=None, event=None):
        """ Set the image for the underlying qt widget """
        pixmap = QPixmap(self.filename)
        self.widget._qwidget.setPixmap(pixmap)
        self.widget.resize()
       
    @property
    def filename(self):
        """ Return the proper filename """
        if os.path.isfile(self._filename):
            return self._filename
        else:
            return self.fileLoader.getProperPath(self._filename)
        