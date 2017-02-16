from PyQt5 import QtGui, QtCore
import sys

class SonglistSortFilterProxyModel(QtCore.QSortFilterProxyModel):

    def __init__(self, source_model, parent=None):
        super(SonglistSortFilterProxyModel, self).__init__(parent)
        self._source_model = source_model
        self.setSourceModel(source_model)

    def track(self, index):
        """
        Returns an instance of model.Track with information about the song to be played. It uses the track() method of
        the source model.
        :param index: QModelIndex
        :return: model.Track that corresponds to the row of the index
        """
        if not index.isValid():
            return QtCore.QVariant()

        source_index = self.mapToSource(index)
        return self.source_model.track(source_index)

    @property
    def source_model(self):
        return self._source_model

    @property
    def table_data(self):
        """
        Returns the full data of the source model.
        :return: data from the source model
        """
        return self.source_model.table_data

    @property
    def table_raw_data(self):
        """
        Returns the full raw data of the source model.
        :return: data from the source model
        """
        return self.source_model.raw_data
