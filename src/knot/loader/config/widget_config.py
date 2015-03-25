
class WidgetConfig:
    """ Represents the configuration for a widget """
    
    def __init__(self, name, painterClassname):
        """ Initialize the widget config with its name and the painter classname """
        self.name = name
        self.painterClassname = painterClassname
        
    def __repr__(self):
        """ Return the string representation of the config """
        return "<WidgetConfig({0}, {1})>".format(self.name, self.painterClassname)