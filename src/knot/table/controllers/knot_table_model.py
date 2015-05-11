from PySide.QtCore import QAbstractTableModel, Qt

class KnotTableModel(QAbstractTableModel):
    """ Represents a table model for use in  """
    
    def __init__(self, columns):
        """ Initialize the Table Model """
        QAbstractTableModel.__init__(self)
        self.columns = columns
        
    def rowCount(self, parent):
        return 1
        
    def columnCount(self, parent):
        return len(self.columns)
        
    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return ''
        
    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.columns[col].header
        return None