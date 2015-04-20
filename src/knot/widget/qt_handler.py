from .qt_value_map import SetContentFnMap, SetValueFnMap, GetValueSignalMap
from knot.events.event_types import WIDGET_CREATED

def BuildQtSetMethod(mapping):
    """ Build the method for the Qt Handler to use a setter function from a QtValueMap """
    
    def set(self, value):
        if self._qwidget in mapping:
            fn = mapping[self._qwidget]
            fn(value)
    return set

class QtHandler:
    """ Handle the underlying Qt widget data for a particular widget """
    setContent = BuildQtSetMethod(SetContentFnMap)
    setValue = BuildQtSetMethod(SetValueFnMap)
    
    def __init__(self, widget):
        """ Initialize the Handler with the tree """
        self.widget = widget
        self._qwidget = None
        
    def hasQWidget(self):
        """ Return if the underlying qt widget has been built """
        return self._qwidget is not None
        
    def setQWidget(self, qwidget, ignoreParent=False):
        """ Set the underlying Qt Widget for this widget """
        self._qwidget = qwidget
        if self.widget.parent is not None and not ignoreParent:
            self._qwidget.setParent(self.widget.parent._qwidget)
        
        self.widget.eventHandler.attachEvents(qwidget)
        self.widget.fire(WIDGET_CREATED)
        
    def getValueSignal(self):
        """ Return the internal qt signal fired when the value of a widget changes """
        if self._qwidget in GetValueSignalMap:
            return GetValueSignalMap[self._qwidget]
        return None
        
    def moveTo(self, *args):
        """ Move the widget to the given position """
        return self._qwidget.move(*args)
        
    def resizeTo(self, *args):
        """ Resize the widget to the given size """
        return self._qwidget.resize(*args)