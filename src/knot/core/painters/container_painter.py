from .painter import Painter
from knot.policy.default_policies_via_class import DefaultPoliciesViaClass
from knot.core.sizing.shrink_to_contents import ShrinkToContents

from PySide.QtGui import QWidget

class ContainerPainter(Painter):
    """ Handles painting a collection of child widgets """
    DEFAULT_SIZING = DefaultPoliciesViaClass(ShrinkToContents)
        
    def buildQWidget(self, widget):
        """ Draw the Widget to use as the container """
        return QWidget()
        
    def afterDrawWidget(self, widget, qwidget):
        """ Perform any necessary actions after drawing the necessary widget """
        self.drawChildren(widget, qwidget)
    
    def drawChildren(self, widget, qwidget):
        """ Draws the children widgets """
        for child in widget.children:
            self.drawChild(child, qwidget)
            
    def drawChild(self, child, qwidget):
        """ Draw the child """
        child.draw()
        child._qwidget.setParent(qwidget)
        child.show()