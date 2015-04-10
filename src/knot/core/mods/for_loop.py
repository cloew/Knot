from knot.knot_service import KnotService
from knot.loader.components_loader import ComponentsLoader
from knot.scope.apply_bindings import apply_knot_bindings
from knot.scope.one_way_binding import OneWayBinding

from copy import copy

class ForLoop:
    """ Represents a for loop that creates its child content for each entry in a list """
    values = OneWayBinding("values")
    app = KnotService('app')
    
    @apply_knot_bindings
    def __init__(self, entryName, values, config, tokens, scope):
        """ Initialize the For Loop """
        self.entryName = entryName
        self.componentsLoader = ComponentsLoader(config)
        self.tokens = tokens
        self.scope = scope
        
    def attachWidget(self, widget):
        """ Attach the widget """
        self.widget = widget
        # app.watch(values, self.addChildren)
        self.addChildren(self.values)
        
    def addChildren(self, values):
        """ Add a child for each value in values """
        for value in values:
            newScope = copy(self.scope)
            setattr(newScope, self.entryName, value)
            self.componentsLoader.loadAll(self.tokens, scope=newScope, onto=self.widget)