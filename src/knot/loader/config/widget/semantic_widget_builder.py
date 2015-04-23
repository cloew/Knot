from knot.widget.semantic_widget import SemanticWidget

class SemanticWidgetBuilder:
    """ Helper class to build Semantic Widgets """
    
    def __init__(self, name):
        """ Initialize the Semantic Widget Builder """
        self.name = name
    
    def build(self, content, controller, mods, *args, **kwargs):
        """ Build the widget """
        return SemanticWidget(self.name, content, controller=controller, mods=mods)