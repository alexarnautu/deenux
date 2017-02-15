from PyQt5 import QtGui, QtCore
import sys

class SonglistSortFilterProxyModel(QtCore.QSortFilterProxyModel):

    def __init__(self, original_model, parent=None):
        super(SonglistSortFilterProxyModel, self).__init__(parent)
        self._model = original_model
        self.setSourceModel(original_model)

    @property
    def table_data(self):
        """
        Returns the full data of the source model.
        :return: data from the source model
        """
        return self._model.table_data
