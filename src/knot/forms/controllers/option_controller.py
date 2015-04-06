from knot import apply_knot_bindings, TwoWayBinding

class OptionController:
    """ Represents an option """
    value = TwoWayBinding("value")
    
    @apply_knot_bindings
    def __init__(self, value):
        """ Initialize the Controller with its value """
        pass