from knot.directions import L2R

class DivController:
    """ Handle the div to determine the proper default policies to use """
    
    def __init__(self, direction=L2R):
        """ Initialize the Controller with the direction to flow in """
        self.direction = direction
        
    def attachWidget(self, widget):
        """ Set the widget's direction """
        widget.direction = self.direction