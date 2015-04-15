from kao_decorators import proxy_for

@proxy_for('widget', ['_qwidget'])
@proxy_for('_qwidget', ['show', 'hide'])
class DisplayHandler:
    """ Handles the aspects of a widget regarding displaying """
    
    def __init__(self, widget):
        """ Initialize with the parent widget """
        self.widget = widget
        
    @property
    def isVisible(self):
        """ Return whether the widget is visisble """
        return self._qwidget.isVisible()
        
    @property
    def isHidden(self):
        """ Return whether the widget is hidden """
        return self._qwidget.isHidden()