
from PyQt5 import QtWidgets, QtCore

from src.components.View import View
from src.components.songlist.SonglistController import SonglistController
from src.components.songlist.SonglistAbstractModel import SonglistAbstractModel
from src.components.songlist.SonglistSortFilterProxyModel import SonglistSortFilterProxyModel


class Songlist(QtWidgets.QWidget, View):

    kEndOfTheWorldIndex = 50000

    def __init__(self, context, *args):
        QtWidgets.QWidget.__init__(self, *args)
        View.__init__(self, context, SonglistController(self, context))
        self.setup()

    def setup_ui(self):
        self.vertical_layout = QtWidgets.QVBoxLayout(self)
        self.search_bar = QtWidgets.QLineEdit(self)
        self.songlist_table = QtWidgets.QTableView()

        self.songlist_abstract_model = SonglistAbstractModel(
            self.controller.context.deezer.me.get_favourite_tracks(0, self.kEndOfTheWorldIndex),
            ["Title", "Artist"])
        self.songlist_proxy_model = SonglistSortFilterProxyModel(self.songlist_abstract_model)

        self.search_bar.setPlaceholderText("Search within tracks")

        # NOTE(mirceadino): If enabling sorting is moved after setting the model, it will cause the table to be sorted
        # by some column initially. This might be wanted in the future, but it isn't for now.
        self.songlist_table.setSortingEnabled(True)
        self.songlist_table.setModel(self.songlist_proxy_model)

        self.songlist_table.setColumnWidth(0, self.width() // 3)
        self.songlist_table.horizontalHeader().setStretchLastSection(True)
        self.songlist_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.songlist_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

        self.vertical_layout.addWidget(self.search_bar)
        self.vertical_layout.addWidget(self.songlist_table)

    def retranslate_ui(self):
        pass

    def create_connections(self):
        ctrl = self.controller
        app = self.context.app

        self.search_bar.textChanged.connect(ctrl.on_searchbar_text_changed)
        self.songlist_table.doubleClicked.connect(ctrl.on_line_double_click)
        self.songlist_table.selectionModel().selectionChanged.connect(ctrl.on_line_selected)

    @property
    def songlist_model(self):
        return self.songlist_abstract_model


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = Songlist()
    widget.show()
    sys.exit(app.exec_())
