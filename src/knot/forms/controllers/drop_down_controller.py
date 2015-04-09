from knot import apply_knot_bindings, TwoWayBinding, KnotService
from knot.events.event_types import CHILD_ADDED, WIDGET_CREATED

class DropDownController:
    """ Controller to handle mapping Drop Down Options to their values """
    app = KnotService('app')
    model = TwoWayBinding("model")
    
    @apply_knot_bindings
    def __init__(self, model):
        """ Initialize the Controller with its model """
        self.widget = None
        self.options = []
        
    def attachWidget(self, widget):
        """ Attach the widget """
        self.widget = widget
        widget.on(WIDGET_CREATED, self.attachSignalAndWatch)
        widget.on(CHILD_ADDED, self.addOptions)
        
    def attachSignalAndWatch(self, widget, event=None):
        """ Attach the signal to the qt signal and the watch to the application """
        self.addOptionsToWidget()
        self.setDisplay(self.model)
        self.app.watch(self, 'model', self.setDisplay)
        widget.getValueSignal().connect(self.setModel)
        
    def setModel(self, index):
        """ Set the model value """
        self.model = self.options[index].value
        
    def setDisplay(self, value):
        """ Set the displayed value """
        values = [option.value for option in self.options]
        
        if value in values:
            index = values.index(value)
            self.widget.setValue(index)
        
    def addOptions(self, widget=None, event=None):
        """ Add the options """
        options = self.widget.getChildrenWithType('option')
        self.options = [option.controller for option in options]
        
        for option in self.options:
            option.textChanged.register(self.changeValue)
        
    def addOptionsToWidget(self):
        """ Add the current options to the Combo Box widget """
        for option in self.options:
            self.widget._qwidget.addItem(option.text)
            
    def changeValue(self, option, text):
        """ Change the given text for the widget """
        index = self.options.index(option)
        self.widget._qwidget.setItemText(index, option.text)
        self.widget.resize()