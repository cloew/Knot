
class Painter:
    """ Handles creation of the underlying Qt widget used by a Knot Widget """
    
    def draw(self, widget):
        """ Draw the widget and perform any housekeeping operations """
        qwidget = self.buildQWidget(widget)
        widget._qwidget = qwidget
        self.afterDrawWidget(widget, qwidget)
        
    def buildQWidget(self, widget):
        """ Build the underlying Qt Widget """
        return None
        
    def afterDrawWidget(self, widget, qwidget):
        """ Perform any necessary actions after drawing the necessary widget """
        return None