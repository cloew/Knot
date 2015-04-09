from knot import has_scope, apply_knot_bindings, TwoWayBinding
from PySide.QtGui import QFileDialog

import os

@has_scope
class FilePickerController:
    """ Provides a widget that uses a file dialog to pick a file """
    filename = TwoWayBinding("filename")
    
    @apply_knot_bindings
    def __init__(self, filename):
        """ Initialize the controller with the filename """
        pass
        
    def openFileDialog(self):
        """ Open the file dialog """
        filename, filter = QFileDialog.getOpenFileName(dir=os.path.dirname(self.filename))
        if not filename == '':
            self.filename = filename