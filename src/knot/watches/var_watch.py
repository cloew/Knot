from kao_xobj import xobj_attrgetter

class VarWatch:
    """ Represents a watch placed on a particular variable of an object """
    
    def __init__(self, obj, varName, callback):
        """ Initialize the Watch with the object and its variable to watch and the callback to fire """
        self.obj = obj
        self.attrGetter = xobj_attrgetter(varName)
        self.previousValue = self.attrGetter(self.obj)
        self.callback = callback
        
    def checkChange(self):
        """ Check if the value has changed """
        value = self.attrGetter(self.obj)
        if value != self.previousValue:
            self.previousValue = value
            self.callback(value)