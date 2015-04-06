from knot import apply_knot_bindings, TwoWayBinding, KnotService
from knot.events.event_types import CHILD_ADDED, WIDGET_CREATED

class ComboboxController:
    """ Controller to handle mapping Combo Box Options to their values """
    app = KnotService('app')
    model = TwoWayBinding("model")
    
    @apply_knot_bindings
    def __init__(self, model):
        """ Initialize the Controller with its model """
        self.widget = None
        self.values = []
        
    def attachWidget(self, widget):
        """ Attach the widget """
        self.widget = widget
        widget.on(WIDGET_CREATED, self.attachSignalAndWatch)
        
    def attachSignalAndWatch(self, widget, event=None):
        """ Attach the signal to the qt signal and the watch to the application """
        self.setDisplay(self.model)
        self.app.watch(self, 'model', self.setDisplay)
        widget.getValueSignal().connect(self.setModel)
        
    def setModel(self, index):
        """ Set the model value """
        self.model = self.values[index]
        
    def setDisplay(self, value):
        """ Set the displayed value """
        if value in self.values:
            index = self.values.index(value)
            self.widget.setValue(index)
        