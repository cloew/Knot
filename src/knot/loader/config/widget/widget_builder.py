from knot.widget.widget import Widget
from ..optional_namespaced_class import OptionalNamespacedClass

class WidgetBuilder:
    """ Helper class to build Widgets """
    
    def __init__(self, name, painterClassname=None):
        """ Initialize the Widget Builder """
        self.name = name
        self.painterClass = OptionalNamespacedClass(painterClassname)
    
    def build(self, content, controller, mods, *args, positionings=None, sizings=None, styling=None, **kwargs):
        """ Build the widget """
        painter = self.painterClass.tryToIntantiateClass(content)
        return Widget(self.name, content, painter=painter, controller=controller, positionings=positionings, sizings=sizings, mods=mods, styling=styling)