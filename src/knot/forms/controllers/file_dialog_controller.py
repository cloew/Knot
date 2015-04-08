from knot import has_scope, apply_knot_bindings, TwoWayBinding
from PySide.QtGui import QFileDialog

@has_scope
class FileDialogController:
    """ Handles opening a file dialog """
    filename = TwoWayBinding("model")
    
    @apply_knot_bindings
    def __init__(self, filename):
        """ Initialize the controller with the filename """
        pass
        
    def openFileDialog(self):
        """ Open the file dialog """
        self.filename, filter = QFileDialog.getOpenFileName()