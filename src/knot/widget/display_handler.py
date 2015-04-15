from knot.events.event_types import WIDGET_CREATED

from kao_decorators import proxy_for

@proxy_for('widget', ['_qwidget'])
class DisplayHandler:
    """ Handles the aspects of a widget regarding displaying """
    
    def __init__(self, widget):
        """ Initialize with the parent widget """
        self.widget = widget
        self.widget.on(WIDGET_CREATED, self.apply)
        self._visible = True
        
    def apply(self, widget=None, event=None):
        """ Apply the current display settings """
        self._qwidget.setVisible(self._visible)
        
    @property
    def visible(self):
        """ Return whether the widget is visible """
        return self._qwidget.isVisible() if self.widget.canMove() else self._visible
        
    @visible.setter
    def visible(self, value):
        """ Set whether the widget is visible """
        self._visible = value
        if self.widget.canMove():
            self.apply()
        
    @property
    def hidden(self):
        """ Return whether the widget is hidden """
        return not self.visible
        
    def show(self):
        """ Set the widget to display """
        self.visible = True
        
    def hide(self):
        """ Set the widget to hide """
        self.visible = False