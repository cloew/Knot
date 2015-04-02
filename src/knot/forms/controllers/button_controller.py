from knot import Signal
from knot.events.event_types import WIDGET_CREATED

class ButtonController:
    """ Controls button to specify what should happen when its pressed """
    
    def __init__(self):
        """ Initialize the Button Controller """
        self.clicked = Signal()
        
    def attachWidget(self, widget):
        """ Attach the widget """
        widget.on(WIDGET_CREATED, self.attachSignal)
        
    def attachSignal(self, widget, event=None):
        """ Attach the signal to the qt signal """
        widget._qtwidget.clicked.connect(self.clicked.emit)