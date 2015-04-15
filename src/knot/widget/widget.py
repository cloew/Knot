from .base_widget import BaseWidget
from .container_handler import ContainerHandler
from .display_handler import DisplayHandler
from .knot_rectangle import KnotRectangle
from .policies_handler import PoliciesHandler
from .positioning_defaults_provider import PositioningDefaultsProvider
from .qt_handler import QtHandler
from .sizing_defaults_provider import SizingDefaultsProvider
from .style_handler import StyleHandler

from knot.core.painters.container_painter import ContainerPainter

from kao_decorators import proxy_for
from smart_defaults import smart_defaults, EvenIfNone, PerCall

@proxy_for('_qwidget', ['sizeHint'])
@proxy_for('containerHandler', ['direction', 'setDirection', 'getDefaultChildrenPolicies', 'getContainerSidePosition'])
@proxy_for('displayHandler', ['show', 'hide', 'isVisible', 'isHidden'])
@proxy_for('qtHandler', ['hasQWidget', 'setQWidget', 'setContent', 'setValue', 'getValueSignal', '_qwidget', 'moveTo', 'resizeTo'])
@proxy_for('rectangle', ['width', 'height', 'left', 'right', 'top', 'bottom', 'getSidePosition', 'setSidePosition'])
@proxy_for('styleHandler', ['setStyling'])
class Widget(BaseWidget):
    """ Represents a widget within Knot """
    
    @smart_defaults
    def __init__(self, widgetType, content=None, painter=EvenIfNone(ContainerPainter()), controller=None,
                       mods=PerCall([]), positionings=None, sizings=None, styling=EvenIfNone('')):
        """ Initialize the widget with its painters and policies """
        self.painter = painter
        self.containerHandler = ContainerHandler(self)
        self.displayHandler = DisplayHandler(self)
        self.rectangle = KnotRectangle(self)
        BaseWidget.__init__(self, widgetType, content=content, controller=controller, mods=mods)
        
        self.positioningDefaults = PositioningDefaultsProvider(self)
        self.positioningHandler = PoliciesHandler(self, self.positioningDefaults, policies=positionings)
        self.sizingHandler = PoliciesHandler(self, SizingDefaultsProvider(self), policies=sizings)
        self.styleHandler = StyleHandler(self, styling)
        self.qtHandler = QtHandler(self)
        
    def draw(self):
        """ Draw the widget """
        self.painter.draw(self)
        
    def canMove(self):
        """ Return if this widget can move """
        return self.hasQWidget()
            
    def resize(self):
        """ Resize the widget """
        [policy.resize(self) for policy in self.sizingHandler.policies]