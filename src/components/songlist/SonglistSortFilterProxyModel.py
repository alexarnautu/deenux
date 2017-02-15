from PyQt5 import QtGui, QtCore
import sys

class SonglistSortFilterProxyModel(QtCore.QSortFilterProxyModel):

    def __init__(self, original_model, parent=None):
        super(SonglistSortFilterProxyModel, self).__init__(parent)
        self._model = original_model
        self.setSourceModel(original_model)

    def rowCount(self, parent):
        return self._model.rowCount(parent)

    def columnCount(self, parent):
        return self._model.columnCount(parent)

    def data(self, index, role):
        return self._model.data(index, role)

    def headerData(self, col, orientation, role):
        return self._model.headerData(col, orientation, role)

    @property
    def table_data(self):
        return self._model.table_data

    @property
    def table_raw_data(self):
        return self._model.table_raw_data
