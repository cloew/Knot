
class DoNothing:
    """ Represents a sizing method that does nothing """
        
    def handlesDimension(self, dimension):
        """ Return if this policy positions widgets in the given dimension """
        return self.dimension is BOTH
    
    def applyToWidget(self, widget):
        """ Apply the policy to the neighbor """
        pass
        
    def resize(self, widget):
        """ Adjust the given widget so it is sized properly """
        pass