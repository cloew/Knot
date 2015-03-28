from ..events.event_types import CHILD_ADDED
from knot.sides import LEFT, RIGHT

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
        self.widget.sizingHandler.apply()
        
    @property
    def siblings(self):
        """ Return the given widget's siblings """
        return [child for child in self.parent.children if child is not self.widget]
        
    def getSiblingOn(self, side):
        """ Return the sibling on the given side """
        if side is LEFT:
            return self.getPreviousSibling()
        elif side is RIGHT:
            return self.getNextSibling()
        else:
            return None
        
    def getPreviousSibling(self):
        """ Return the previous sibling of this widget """
        siblings = self.parent.children
        currentWidgetIndex = siblings.index(self.widget)
        if currentWidgetIndex == 0:
            return None
        else:
            return siblings[currentWidgetIndex-1]
        
    def getNextSibling(self):
        """ Return the next sibling of this widget """
        siblings = self.parent.children
        currentWidgetIndex = siblings.index(self.widget)
        if currentWidgetIndex == (len(siblings)-1):
            return None
        else:
            return siblings[currentWidgetIndex+1]