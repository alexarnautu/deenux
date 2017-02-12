
from PyQt5 import QtWidgets, QtCore

from src.components.View import View
from src.components.player.PlayerController import PlayerController
from src.components.player.trackinfo.Trackinfo import Trackinfo
from src.components.player.trackcontrols.Trackcontrols import Trackcontrols


class Player(QtWidgets.QWidget, View):

    def __init__(self, context, *args):
        QtWidgets.QWidget.__init__(self, *args)
        View.__init__(self, context, PlayerController(self, context))
        self.setup()

        self.context.player = self
        self.active = False

    def setup_ui(self):
        h_layout = QtWidgets.QHBoxLayout(self)
        self.track_info = Trackinfo(self.context)
        self.track_controls = Trackcontrols(self.context)
        self.track_controls.setMinimumWidth(230)

        h_layout.addWidget(self.track_controls, 1)
        h_layout.addWidget(self.track_info, 3)

    def retranslate_ui(self):
        pass

    def create_connections(self):
        app = self.context.app
        ctrl = self.controller
        app.DZ_PLAYER_EVENT_QUEUELIST_LOADED.connect(ctrl.on_track_content_loaded)
        app.DZ_PLAYER_EVENT_RENDER_TRACK_START.connect(ctrl.on_track_play_start)

        app.DZ_PLAYER_EVENT_RENDER_TRACK_PAUSED.connect(ctrl.on_track_pause)
        app.DZ_PLAYER_EVENT_LIMITATION_FORCED_PAUSE.connect(ctrl.on_track_pause)
        app.DZ_PLAYER_EVENT_RENDER_TRACK_RESUMED.connect(ctrl.on_track_resume)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = Player({})
    widget.show()
    sys.exit(app.exec_())
