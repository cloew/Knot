from knot import KnotService
from knot.events.event_types import WIDGET_CREATED

class WatchContent:
    """ Mod to set the text for a widget when its content changes """
    app = KnotService('app')
        
    def attachWidget(self, widget):
        """ Attach the widget """
        self.widget = widget
        widget.on(WIDGET_CREATED, self.attachChangeText)
        
    def attachChangeText(self, widget, event=None):
        """ Attach the signal to the qt signal """
        content = widget.painter.content
        content.addWatch(self.app)
        content.changed.register(self.changeText)
        
    def changeText(self, text):
        """ Update the widget's text """
        self.widget._qwidget.setText(text)
        self.widget.resizeWithPolicies()