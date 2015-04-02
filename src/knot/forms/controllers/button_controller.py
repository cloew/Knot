from knot import Signal
from knot.events.event_types import WIDGET_CREATED
from knot.core.controllers.set_text_controller import SetTextController

class ButtonController(SetTextController):
    """ Controls button to specify what should happen when its pressed """
    
    def __init__(self):
        """ Initialize the Button Controller """
        SetTextController.__init__(self)
        self.clicked = Signal()
        
    def attachWidget(self, widget):
        """ Attach the widget """
        SetTextController.attachWidget(self, widget)
        widget.on(WIDGET_CREATED, self.attachSignal)
        
    def attachSignal(self, widget, event=None):
        """ Attach the signal to the qt signal """
        widget._qwidget.clicked.connect(self.clicked.emit)