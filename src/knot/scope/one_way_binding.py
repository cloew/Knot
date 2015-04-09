from .scoped_value import ScopedValue

class OneWayBinding:
    """ Represents a scoped value or a static value """
    
    def __init__(self, argName):
        """ Initialize the One Way Binding """
        self.argName = "_knotscope_{0}".format(argName)
        
    def applyKnotBinding(self, obj, scopedValue):
        """ Apply the knot binding to the given object """
        setattr(obj, self.argName, scopedValue)
    
    def __get__(self, obj, objtype=None):
        """ Return the value """
        return self.getValue(obj) if obj is not None else self
        
    def getValue(self, obj):
        """ Return the value """
        value = getattr(obj, self.argName)
        if value.__class__ is ScopedValue:
            value = value.get()
        return value