from .base_widget import BaseWidget

class SemanticWidget(BaseWidget):
    """ Represents a widget that is purley semantic and has no underlying Qt Widget """
        
    def draw(self):
        """ Draw the widget """
        pass
        
    @property
    def visible(self):
        """ Return false since semantic widgets should never be visible """
        return False
        
    def geometry(self):
        """ Retutn the geometry """
        return None