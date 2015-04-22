from .base_widget import BaseWidget
from knot.events.event_types import PARENT_ADDED

class PassthroughWidget(BaseWidget):
    """ Represents a widget that should not take up a spot in the widget tree """
    
    def __init__(self, *args, **kwargs):
        """ Initialize the widget """
        BaseWidget.__init__(self, *args, **kwargs)
        self.on(PARENT_ADDED, self.addAllChildrenToParent)
    
    def addChild(self, child):
        """ Add the given child to this widget's parent """
        self.children.append(child)
        if self.parent is not None:
            self.parent.addChild(child)
            
    def addAllChildrenToParent(self, widget=None, value=None):
        """ Add all children of this widget to the parent widget """
        for child in self.children:
            self.parent.addChild(child)
        
    @property
    def visible(self):
        """ Return false since semantic widgets should never be visible """
        return False
        
    def geometry(self):
        """ Retutn the geometry """
        return None