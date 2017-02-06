from PyQt5 import QtWidgets
from src.AppContext import AppContext
from src.deenuxapi.deezer.DeezerProvider import DeezerProvider
from src.components.player.Player import Player
from src.components.songlist.Songlist import Songlist
import asyncio
import sys

class Application:

    def __init__(self):
        self.init_context()

    def launch (self):

        app = QtWidgets.QApplication(sys.argv)
        self.setup_ui()
        self.create_connections()

        self._main_window.show()
        sys.exit(app.exec_())

    def init_context(self):
        self.context = AppContext (
            deezer = DeezerProvider(DeezerProvider.authorize()),
            event_loop = asyncio.get_event_loop()
        )

    def setup_ui(self):
        self._main_window = window = QtWidgets.QWidget()
        self.context.hook(main_window = window)

        main_layout = QtWidgets.QVBoxLayout()
        center_layout = QtWidgets.QHBoxLayout()

        self.player = Player(self.context)

        main_layout.addLayout(center_layout)
        main_layout.addWidget(self.player)

        self.songlist = Songlist(self.context)
        center_layout.addWidget(self.songlist)

        window.setLayout(main_layout)


    def create_connections(self):
        pass