
class TwoWayBinding:
    """ Represents a scoped value that is still tied to the original scope value """
    
    def __init__(self, argName):
        """ Initialize the Two Way Binding """
        self.argName = "_knotscope_{0}".format(argName)
        
    def applyKnotBinding(self, obj, scopedValue):
        """ Apply the knot binding to the given object """
        setattr(obj, self.argName, scopedValue)
    
    def __get__(self, obj, objtype=None):
        """ Return the value """
        return self.getScopedValue(obj).get() if obj is not None else self
        
    def __set__(self, obj, value):
        """ Set the value """
        self.getScopedValue(obj).set(value)
        
    def getScopedValue(self, obj):
        """ Return the scoped value """
        return getattr(obj, self.argName)