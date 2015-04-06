
from PySide.QtGui import QLabel, QLineEdit, QPushButton

class QtContentHandler:
    """ Handles getting and setting the content value of a Qt Widget """
    QT_WIDGET_TO_SET_FN = {QLabel: QLabel.setText,
                           QLineEdit: QLineEdit.setText,
                           QPushButton: QPushButton.setText}
                           
    def setValue(self, qwidget, value):
        """ Set the Qt Widget value """
        if qwidget.__class__ in self.QT_WIDGET_TO_SET_FN:
            fn = self.QT_WIDGET_TO_SET_FN[qwidget.__class__]
            fn(qwidget, value)