from kao_xobj import xobj_attrgetter, xobj_attrsetter

class ScopedValue:
    """ Represents a value to be retrieved and set on the scope """
    
    def __init__(self, scope, attrName):
        """ Initialize the Scoped Value with the scope and attribute to wrap """
        self.scope = scope
        self.getter = xobj_attrgetter(attrName)
        self.setter = xobj_attrsetter(attrName)
        
    def get(self):
        """ Return the current value """
        return self.getter(self.scope)
        
    def set(self, value):
        """ Set the value """
        return self.setter(self.scope, value)