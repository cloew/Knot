from knot import apply_knot_bindings, KnotService, Signal, TwoWayBinding

class OptionController:
    """ Represents an option """
    app = KnotService('app')
    value = TwoWayBinding("value")
    
    @apply_knot_bindings
    def __init__(self, value):
        """ Initialize the Controller with its value """
        self.textChanged = Signal()
        self.widget = None
        self.app.watch(self, 'text', self.fireSignal)
        
    def attachWidget(self, widget):
        """ Attach the widget """
        self.widget = widget
        
    @property
    def text(self):
        """ Return the text for this option """
        text = self.value
        if self.widget is not None and self.widget.content is not None:
            text = self.widget.content.text
        return text
        
    def fireSignal(self, text):
        """ Fire the text changed signal """
        self.textChanged.emit(self, text)