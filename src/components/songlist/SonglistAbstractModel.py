from PyQt5 import QtGui, QtCore
import sys

class SonglistAbstractModel(QtCore.QAbstractTableModel):

    def __init__(self, data, header, parent=None):
        super(SonglistAbstractModel, self).__init__(parent)

        # Processing the data for display
        self._raw_data = data
        self._data = list(map(lambda t : [t, t.title, t.artist.name], data))
        self._header = header

    def rowCount(self, parent):
        return len(self._data)

    def columnCount(self, parent):
        return len(self._header)

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

    def track(self, index):
        """
        Returns an instance of model.Track with information about the song to be played.
        :param index: QModelIndex
        :return: model.Track that corresponds to the row of the index
        """
        if not index.isValid():
            return QtCore.QVariant()

        row = index.row()
        return self._data[row][0]

    @property
    def table_data(self):
        return self._data

    @property
    def table_raw_data(self):
        return self._raw_data
