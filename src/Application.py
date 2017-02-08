from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject
from src.AppContext import AppContext
from src.deenuxapi.deezer.DeezerProvider import DeezerProvider
from src.components.player.Player import Player
from src.components.songlist.Songlist import Songlist
from src.components.sidemenu.Sidemenu import Sidemenu
from src.components.toolbar.Toolbar import Toolbar
import sys


class Application(QObject):

    """ You have to add static pyqtSignals MANUALLY
        You won't be able to connect them if you add them dynamically with setattr
        When you need a jukebox event, just add them here as a signal
    """
    DZ_PLAYER_EVENT_QUEUELIST_LOADED = pyqtSignal(object, str, bool, bool, name='DZ_PLAYER_EVENT_QUEUELIST_LOADED')
    DZ_PLAYER_EVENT_RENDER_TRACK_START = pyqtSignal(object, str, bool, bool, name='DZ_PLAYER_EVENT_RENDER_TRACK_START')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_context()

    def launch (self):

        app = QtWidgets.QApplication(sys.argv)
        self.setup_ui()
        self.create_connections()
        self.connect_wrapper_events()

        self._main_window.show()
        sys.exit(app.exec_())

    def connect_wrapper_events(self):
        jb = self.context.deezer.jukebox

        # Connecting player events
        for ev_name in filter(lambda a : a.startswith('DZ_'), vars(Application).keys()):
            jb.on(ev_name, self.emit_wrapper_signal)

    def emit_wrapper_signal(self, event_name, *event_args):
        getattr(self, event_name).emit(*event_args)

    def init_context(self):
        self.context = AppContext (
            deezer = DeezerProvider(DeezerProvider.authorize()),
            app = self
        )

    def setup_ui(self):
        self._main_window = window = QtWidgets.QWidget()
        self.context.hook(main_window = window)

        main_layout = QtWidgets.QVBoxLayout()
        center_layout = QtWidgets.QHBoxLayout()

        self.player = Player(self.context)
        self.sidemenu = Sidemenu(self.context)
        self.toolbar = Toolbar(self.context)
        self.songlist = Songlist(self.context)

        main_layout.addWidget(self.toolbar)
        main_layout.addLayout(center_layout)
        main_layout.addWidget(self.player)

        center_layout.addWidget(self.sidemenu)
        center_layout.addWidget(self.songlist)

        window.setLayout(main_layout)

    def create_connections(self):
        pass
