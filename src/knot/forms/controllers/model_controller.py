from knot import apply_knot_bindings, TwoWayBinding, KnotService
from knot.events.event_types import WIDGET_CREATED

class ModelController:
    """ Controller to handle setting a value on a model attribute """
    app = KnotService('app')
    model = TwoWayBinding("model")
    
    @apply_knot_bindings
    def __init__(self, model):
        """ Initialize the Controller with its model """
        pass
        
    def attachWidget(self, widget):
        """ Attach the widget """
        self.widget = widget
        widget.on(WIDGET_CREATED, self.attachSignalAndWatch)
        
    def attachSignalAndWatch(self, widget, event=None):
        """ Attach the signal to the qt signal and the watch to the application """
        self.setDisplay(self.model)
        self.app.watch(self, 'model', self.setDisplay)
        widget.getValueSignal().connect(self.setModel)
        
    def setModel(self, text):
        """ Set the model value """
        self.model = text
        
    def setDisplay(self, value):
        """ Set the model value """
        self.widget.setValue(value)