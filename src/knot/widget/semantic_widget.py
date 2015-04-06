from .tree_handler import TreeHandler
from ..events.event_handler import EventHandler

from kao_decorators import proxy_for
from smart_defaults import smart_defaults, PerCall

@proxy_for('eventHandler', ['fire', 'on', 'unregister'])
@proxy_for('treeHandler', ['parent', 'children', 'siblings', 'addChild', 'attachToParent', 'getSiblingOn', 'getPreviousSibling'])

class SemanticWidget:
    """ Represents a widget that is purley semantic and has no underlying Qt Widget """
    
    @smart_defaults
    def __init__(self, controller=None, mods=PerCall([])):
        """ Initialize the widget """
        self.controller = controller
        self.mods = mods
        self.eventHandler = EventHandler(self)
        self.treeHandler = TreeHandler(self)
        
        thingsToAttach = self.mods if self.controller is None else [self.controller] + self.mods
        for thing in thingsToAttach:
            if hasattr(thing, 'attachWidget'):
                thing.attachWidget(self)
        
    def draw(self):
        """ Draw the widget """
        pass