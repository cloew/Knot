from knot import KnotService
from knot.events.event_types import PARENT_ADDED, WIDGET_CREATED

class TooltipController:
    """ Handles adding a tooltip to a widget """
    app = KnotService('app')
        
    def attachWidget(self, widget):
        """ Attach to the widget """
        self.widget = widget
        self.widget.on(PARENT_ADDED, self.trackParent)
        
    def trackParent(self, widget=None, event=None):
        """ Track the parent widget """
        self.widget.parent.on(WIDGET_CREATED, self.addTooltip)
        if self.widget.content is not None:
            self.widget.content.addWatch(self.app)
            self.widget.content.changed.register(self.addTooltip)
        
    def addTooltip(self, widget=None, event=None):
        """ Add a tooltip to the parent widget """
        self.widget.parent._qwidget.setToolTip(self.text)
        
    @property
    def text(self):
        """ Return the text for the content """
        return self.widget.content.text if self.widget.content is not None else ''