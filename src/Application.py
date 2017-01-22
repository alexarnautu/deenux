from PyQt5 import QtWidgets
from src.AppContext import AppContext
from src.deenuxapi.Provider import Provider
from src.components.player.Player import Player
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
            deezerService = Provider("deezer")
        )

    def setup_ui(self):
        self._main_window = window = QtWidgets.QMainWindow()
        main_layout = QtWidgets.QVBoxLayout()

        self.player = Player(self.context, window)

        main_layout.addWidget(self.player)
        window.setLayout(main_layout)


    def create_connections(self):
        pass