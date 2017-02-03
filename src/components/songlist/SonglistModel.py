from PyQt5 import QtGui, QtCore
import sys

class SonglistModel(QtCore.QAbstractTableModel):

    def __init__(self, data, header, parent=None):
        super(SonglistModel, self).__init__(parent)

        # Processing the data for display
        self._data = list(map(lambda t : [t, t.title, t.artist.name], data))
        self._header = header

    def rowCount(self, parent):
        return len(self._data)

    def columnCount(self, parent):
        return 2

    def data(self, index, role):
        if not index.isValid() or role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        row = index.row()
        col = index.column()
        return self._data[row][col + 1]

    def headerData(self, col, orientation, role):
        if orientation != QtCore.Qt.Horizontal or role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        
        return self._header[col]

    @property
    def table_data(self):
        return self._data
