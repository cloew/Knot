from knot import apply_knot_bindings, KnotService, Signal, TwoWayBinding

class OptionController:
    """ Represents an option """
    app = KnotService('app')
    value = TwoWayBinding("value")
    
    @apply_knot_bindings
    def __init__(self, value):
        """ Initialize the Controller with its value """
        self.textChanged = Signal()
        self.app.watch(self, 'text', self.fireSignal)
        
    @property
    def text(self):
        """ Return the text for this option """
        return self.value
        
    def fireSignal(self, text):
        """ Fire the text changed signal """
        self.textChanged.emit(self, text)