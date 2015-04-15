from knot.knot_service import KnotService
from knot.loader.components_loader import ComponentsLoader
from knot.scope.apply_bindings import apply_knot_bindings
from knot.scope.one_way_binding import OneWayBinding

class DisplayIf:
    """ Represents a modifier that conditionally hides or displays the widget """
    conditionValue = OneWayBinding("conditionValue")
    app = KnotService('app')
    
    @apply_knot_bindings
    def __init__(self, conditionValue):
        """ Initialize with the condition value """
        
    def attachWidget(self, widget):
        """ Attach the widget """
        self.widget = widget
        self.app.watch(self, 'conditionValue', self.setDisplay)
        self.setDisplay(self.conditionValue)
        
    def setDisplay(self, value):
        """ Set the display settings for the widget """
        self.widget.visible = value