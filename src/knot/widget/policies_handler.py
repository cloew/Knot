from ..events.event_types import PARENT_ADDED
from knot.dimensions import HORIZONTAL, VERTICAL, BOTH

from smart_defaults import smart_defaults, EvenIfNone, PerCall

class PoliciesHandler:
    """ Handles the policies for the parent widget """
    
    @smart_defaults
    def __init__(self, widget, defaultsProvider, policies=EvenIfNone(PerCall([]))):
        """ Initialize the Handler with the widget and its positioning policy """
        self.widget = widget
        self.defaultsProvider = defaultsProvider
        self.policies = policies
        self.widget.on(PARENT_ADDED, self.apply)
        
    def apply(self, widget=None, event=None):
        """ Apply the positionig policy """
        policies = self.getProperPolicies()
        for policy in policies:
            policy.applyToWidget(self.widget)
            
    def getProperPolicies(self):
        """ Get proper policies """
        if len(self.policies) == 0:
            self.policies = self.defaultsProvider.getDefaultPolicies(BOTH)
            
        fulfilledDimensions = self.getFulfilledDimensions()
        
        for dimension in [HORIZONTAL, VERTICAL]:
            if dimension not in fulfilledDimensions:
                self.policies += self.defaultsProvider.getDefaultPolicies(dimension)
        return self.policies
            
    def getFulfilledDimensions(self):
        """ Return the dimensions that have been fulfilled by the current policies """
        fulfilledDimensions = set()
        
        for policy in self.policies:
            for dimension in [HORIZONTAL, VERTICAL]:                
                if policy.handlesDimension(dimension):
                    fulfilledDimensions.add(dimension)
        return fulfilledDimensions