from knot.scope.knot_scope import KnotScope

from PySide.QtCore import QAbstractTableModel, Qt
from copy import copy

class KnotTableModel(QAbstractTableModel):
    """ Represents a table model for use in  """
    
    def __init__(self, records, columns):
        """ Initialize the Table Model """
        QAbstractTableModel.__init__(self)
        self.records = records
        self.columns = columns
        
        self.scopes = []
        for i, record in enumerate(self.records):
            scope = KnotScope()
            scope.record = record
            scope.row = i
            self.scopes.append(scope)
        
    def rowCount(self, parent):
        return len(self.records)
        
    def columnCount(self, parent):
        return len(self.columns)
        
    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.columns[index.column()].getData(self.scopes[index.row()])
        
    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.columns[col].header
        return None