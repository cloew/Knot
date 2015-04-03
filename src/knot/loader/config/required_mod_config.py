from kao_modules import NamespacedClass

class RequiredModConfig:
    """ Represents the configuration for a Mod Required for a widget """
    
    def __init__(self, classname):
        """ Initialize the Config with the mod classname to generate """
        self.modClassname = classname
        self.namespacedClass = NamespacedClass(self.modClassname)
        
    def build(self, *args, **kwargs):
        """ Return the proper policy object """
        return self.namespacedClass.instantiate(*args, **kwargs)
        
    def __repr__(self):
        """ Return the string representation of the config """
        return "<RequiredModConfig({0})>".format(self.modClassname)