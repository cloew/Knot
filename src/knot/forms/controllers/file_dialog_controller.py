from knot import has_scope
from PySide.QtGui import QFileDialog

@has_scope
class FileDialogController:
    """ Handles opening a file dialog """
    
    def __init__(self):
        """ Initialize the controller with the *** """
        self.filename = ''
        
    def openFileDialog(self):
        """ Open the file dialog """
        self.filename, filter = QFileDialog.getOpenFileName()