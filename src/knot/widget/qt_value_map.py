from PySide.QtGui import QLabel, QLineEdit, QPushButton

QT_WIDGET_TO_SET_CONTENT_FN = {QLabel: 'setText',
                               QLineEdit: 'setText',
                               QPushButton: 'setText'}

class QtValueMap:
    """ Maps a Qt Widget class to its corresponding attribute """
    
    def __init__(self, mapping):
        """ Initialize the Qt Value Map with its mapping """
        self.mapping = mapping
        
    def __contains__(self, qwidget):
        """ Return if the widget is in the mapping """
        return qwidget.__class__ in self.mapping
        
    def __getitem__(self, qwidget):
        """ Return the value for the given widget's class """
        return getattr(qwidget, self.mapping[qwidget.__class__])
            
SetContentFnMap = QtValueMap(QT_WIDGET_TO_SET_CONTENT_FN)