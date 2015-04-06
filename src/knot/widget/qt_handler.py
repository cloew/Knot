from .qt_value_map import SetContentFnMap
from knot.events.event_types import WIDGET_CREATED

class QtHandler:
    """ Handle the underlying Qt widget data for a particular widget """
    
    def __init__(self, widget):
        """ Initialize the Handler with the tree """
        self.widget = widget
        self._qwidget = None
        
    def hasQWidget(self):
        """ Return if the underlying qt widget has been built """
        return self._qwidget is not None
        
    def setQWidget(self, qwidget):
        """ Set the underlying Qt Widget for this widget """
        self._qwidget = qwidget
        self.widget.eventHandler.attachEvents(qwidget)
        self.widget.fire(WIDGET_CREATED)
        
    def setContent(self, value):
        """ Set the content of the widget """
        if self._qwidget in SetContentFnMap:
            fn = SetContentFnMap[self._qwidget]
            fn(value)