from .widget_tracker import WidgetTracker

class ParentTracker(WidgetTracker):
    """ Helper class to track events on a widget's parent """
    
    def getSubject(self, widget):
        """ Return the subject for the events """
        return widget.parent