from knot.widget.passthrough_widget import PassthroughWidget

class PassthroughWidgetBuilder:
    """ Helper class to build Passthrough Widgets """
    
    def __init__(self, name, painterClassname=None):
        """ Initialize the Passthrough Widget Builder """
        self.name = name
    
    def build(self, content, controller, mods, *args, **kwargs):
        """ Build the widget """
        return PassthroughWidget(self.name, content, controller=controller, mods=mods)