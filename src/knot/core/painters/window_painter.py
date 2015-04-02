from .container_painter import ContainerPainter
from ..sizing.do_nothing import DoNothing
from knot.dimensions import BOTH
from knot.policy.default_policies import DefaultPolicies

from PySide.QtGui import QMainWindow

class WindowPainter(ContainerPainter):
    """ Handles creation of the Qt widget to represent the window """
    DEFAULT_SIZING = DefaultPolicies({BOTH:DoNothing()})
        
    def buildQWidget(self, widget):
        """ Draw the Main Window and tell it to maximize """
        qwidget = QMainWindow()
        qwidget.showMaximized()
        return qwidget