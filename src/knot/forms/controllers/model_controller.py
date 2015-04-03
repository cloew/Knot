from knot import apply_knot_bindings, TwoWayBinding
from knot.events.event_types import WIDGET_CREATED

class ModelController:
    """ Controller to handle setting a value on a model attribute """
    model = TwoWayBinding("model")
    
    @apply_knot_bindings
    def __init__(self, model):
        """ Initialize the Controller with its model """
        pass
        
    def attachWidget(self, widget):
        """ Attach the widget """
        widget.on(WIDGET_CREATED, self.attachSignal)
        
    def attachSignal(self, widget, event=None):
        """ Attach the signal to the qt signal """
        widget._qwidget.textChanged.connect(self.setModel)
        
    def setModel(self, text):
        """ Set the model value """
        self.model = text