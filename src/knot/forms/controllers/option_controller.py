from knot import apply_knot_bindings, KnotService, Signal, TwoWayBinding

class OptionController:
    """ Represents an option """
    app = KnotService('app')
    value = TwoWayBinding("value")
    
    @apply_knot_bindings
    def __init__(self, value):
        """ Initialize the Controller with its value """
        self.valueChanged = Signal()
        self.app.watch(self, 'value', self.fireSignal)
        
    def fireSignal(self, value):
        """ Fire the value changed signal """
        self.valueChanged.emit(self, value)