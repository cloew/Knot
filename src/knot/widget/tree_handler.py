from ..events.event_types import CHILD_ADDED, PARENT_ADDED
from knot.directions import L2R
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
        self.widget.fire(PARENT_ADDED)
        
    def getChildrenWithType(self, widgetType):
        """ Return the widget's children with the given type """
        return [child for child in self.children if child.widgetType == widgetType]
        
    @property
    def siblings(self):
        """ Return the given widget's siblings """
        return [child for child in self.parent.children if child is not self.widget]
        
    @property
    def containerDirection(self):
        """ Return the direction of this widget's parent """
        return self.widget.parent.direction if self.widget.parent is not None else self.widget.direction
        
    def getSiblingOn(self, side):
        """ Return the sibling on the given side """
        if side.dimension is self.containerDirection.dimension:
            if side is self.containerDirection.startingSide:
                return self.getPreviousSibling()
            else:
                return self.getNextSibling()
        else:
            return None
        
    def getPreviousSibling(self):
        """ Return the previous sibling of this widget """
        if self.widget.isHidden:
            return None
            
        siblings = self.visibleSiblings
        currentWidgetIndex = siblings.index(self.widget)
        if currentWidgetIndex == 0:
            return None
        else:
            return siblings[currentWidgetIndex-1]
        
    def getNextSibling(self):
        """ Return the next sibling of this widget """
        if self.widget.isHidden:
            return None
            
        siblings = self.visibleSiblings
        currentWidgetIndex = siblings.index(self.widget)
        if currentWidgetIndex == (len(siblings)-1):
            return None
        else:
            return siblings[currentWidgetIndex+1]
            
    @property
    def visibleSiblings(self):
        """ Return the visible siblings """
        return [child for child in self.parent.children if child.isVisible]