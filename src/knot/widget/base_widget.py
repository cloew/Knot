from .container_handler import ContainerHandler
from .qt_handler import QtHandler
from .tree_handler import TreeHandler
from ..events.event_handler import EventHandler

from kao_decorators import proxy_for
from smart_defaults import smart_defaults, PerCall

@proxy_for('_qwidget', ['sizeHint', 'geometry'])
@proxy_for('containerHandler', ['direction', 'setDirection', 'getDefaultChildrenPolicies', 'getContainerSidePosition'])
@proxy_for('eventHandler', ['fire', 'on', 'unregister'])
@proxy_for('qtHandler', ['hasQWidget', 'setQWidget', 'setContent', 'setValue', 'getValueSignal', '_qwidget', 'moveTo', 'resizeTo'])
@proxy_for('treeHandler', ['parent', 'children', 'siblings', 'addChild', 'attachToParent', 'getChildrenWithType', 'getSiblingOn', 'getPreviousSibling'])
class BaseWidget:
    """ Represents the base widget functionality """
    
    @smart_defaults
    def __init__(self, widgetType, content=None, controller=None, mods=PerCall([])):
        """ Initialize the widget """
        self.widgetType = widgetType
        self.content = content
        self.controller = controller
        self.mods = mods
        self.containerHandler = ContainerHandler(self)
        self.eventHandler = EventHandler(self)
        self.qtHandler = QtHandler(self)
        self.treeHandler = TreeHandler(self)
        
        thingsToAttach = self.mods if self.controller is None else [self.controller] + self.mods
        for thing in thingsToAttach:
            self.attachWidgetToMod(thing)
        
    def addMod(self, mod):
        """ Add the mod  """
        self.mods.append(mod)
        self.attachWidgetToMod(mod)
        
    def attachWidgetToMod(self, mod):
        if hasattr(mod, 'attachWidget'):
            mod.attachWidget(self)
            
    def __repr__(self):
        """ Return the string representation of this widget """
        return "<{0}({1})>".format(self.__class__.__name__, self.widgetType)