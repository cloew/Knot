from .container_painter import ContainerPainter
from .positioning.left_to_right import LeftToRight
from .sizing.shrink_to_contents import ShrinkToContents

from PySide.QtGui import QWidget

class LeftToRightPainter(ContainerPainter):
    """ Handles creation of a Qt widget for wrapping chidlren widgets that are placed horizontally """
    
    def __init__(self, content, sizing=ShrinkToContents()):
        """ Initialize the painter """
        ContainerPainter.__init__(self, sizing, LeftToRight())
        
    def buildQWidget(self, widget):
        """ Draw the Widget to use as the container """
        return QWidget()
        
    def afterDrawWidget(self, widget, qwidget):
        """ Use the Container Painter's after draw then shrink this widget so it fits its children exactly """
        ContainerPainter.afterDrawWidget(self, widget, qwidget)
        # self.shrinkContainer(widget, qwidget)
        
    def shrinkContainer(self, widget, qwidget):
        """ Shrink the container widget so it exactly fits its contents """
        ShrinkToContents().adjust(widget)