from ..events.event_types import CHILD_ADDED

class TreeHandler:
    """ Handle Widget Tree data for a particular widget """
    
    def __init__(self, widget):
        """ Initialize the Handler with the tree """
        self.widget = widget
        self.parent = None
        self.children = []
        
    def addChild(self, child):
        """ Add the Child to this widget """
        self.children.append(child)
        child.attachToParent(self.widget)
        self.widget.fire(CHILD_ADDED, event=child)
        
    def attachToParent(self, parent):
        """ Add the Child to this widget """
        self.parent = parent
        self.widget.positioningHandler.apply()
        if self.widget.sizing is not None:
            self.widget.sizing.applyToWidget(self.widget)
        
    @property
    def siblings(self):
        """ Return the given widget's siblings """
        return [child for child in self.parent.children if child is not self.widget]