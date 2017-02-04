
from PyQt5 import QtWidgets, QtCore
from src.components.songlist.SonglistController import SonglistController
from src.components.songlist.SonglistModel import SonglistModel


class Songlist(QtWidgets.QWidget):

    def create_connections(self):
        pass

    @property
    def controller(self):
        return self._controller

    def __init__(self, *args):
        super(Songlist, self).__init__(*(args[1:]))
        self._controller = SonglistController(args[0])

        self.setup_ui()
        self.retranslate_ui()
        self.create_connections()

    def setup_ui(self):
        self.horizontal_layout = QtWidgets.QHBoxLayout(self)
        self.songlist_table = QtWidgets.QTableView()
        self.songlist_model = SonglistModel(self.controller.context.deezer_service.get_favourite_tracks(0, 50000), ["Title", "Artist"])
        self.songlist_table.setModel(self.songlist_model)

        self.songlist_table.setColumnWidth(0, self.width() // 3)
        self.songlist_table.horizontalHeader().setStretchLastSection(True)

        self.horizontal_layout.addWidget(self.songlist_table)

    def retranslate_ui(self):
        pass

    def create_connections(self):
        self.songlist_table.doubleClicked.connect(self.controller.on_line_double_click)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = Songlist()
    widget.show()
    sys.exit(app.exec_())