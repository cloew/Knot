from knot.dimensions import HORIZONTAL, VERTICAL, BOTH
from knot.events.event_types import MOVED, RESIZED
from knot.events.tracker.children_tracker import ChildrenTracker

class ShrinkToContents:
    """ Represents sizing a widget by making it fit its contents exactly """
    
    def __init__(self, dimension=BOTH):
        """ Initialize the Centerer """
        self.dimension = dimension
        self.childrenTracker = ChildrenTracker([MOVED, RESIZED], self.resize)
        
    def handlesDimension(self, dimension):
        """ Return if this policy positions widgets in the given dimension """
        return self.dimension is BOTH or dimension is self.dimension
    
    def applyToWidget(self, widget):
        """ Apply the policy to the neighbor """
        self.childrenTracker.apply(widget)
        
    def resize(self, widget):
        """ Adjust the given widget so it is sized properly """
        width = widget.width
        height = widget.height
        
        if self.dimension is BOTH or self.dimension is HORIZONTAL:
            width = self.getWidth(widget)
        if self.dimension is BOTH or self.dimension is VERTICAL:
            height = self.getHeight(widget)
            
        widget.resizeTo(width, height)
        
    def getWidth(self, widget):
        """ Return the proper width for the widget """
        return self._getDimensionValue(widget, 'width', HORIZONTAL)
        
    def getHeight(self, widget):
        """ Return the proper height for the widget """
        return self._getDimensionValue(widget, 'height', VERTICAL)
        
    def _getDimensionValue(self, widget, fieldName, dimension):
        """ Return the dimension value for the widget """
        value = 0
        if len(widget.children) > 0:
            values = [getattr(child, fieldName) for child in widget.children]
            if widget.direction.dimension is dimension:
                value = sum(values)
            else:
                value = max(values)
        return value