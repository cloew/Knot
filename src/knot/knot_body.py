from .widget.widget import Widget

window_widgets = ['body', 'menu-bar', 'status-bar']

class KnotBody(Widget):
    """ Represents the body widget of the application """
    
    def __init__(self):
        """ Initialize the body """
        Widget.__init__(self, 'body')
            
    def addChild(self, child):
        """ Add the child """
        if child.widgetType in window_widgets:
            self.parent.addChild(child)
        else:
            super().addChild(child)