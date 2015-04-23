from kao_modules import NamespacedClass

class OptionalNamespacedClass:
    """ Represents a namespaced class that is optionally provided """
    
    def __init__(self, classname):
        """ Initialize with the classname """
        self.classname = classname
        self.namespacedClass = self.tryToBuildNamespacedClass(classname)
        
    def tryToBuildNamespacedClass(self, classname):
        """ Build the Namespaced Class object for the given name if the name is not None """
        return None if classname is None else NamespacedClass(classname)
        
    def tryToIntantiateClass(self, *args, **kwargs):
        """ Instantiate the Namespaced Class object """
        return None if self.namespacedClass is None else self.namespacedClass.instantiate(*args, **kwargs)
        
    def __repr__(self):
        """ Return a string representation """
        return self.classname