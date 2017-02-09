
from PyQt5 import QtWidgets, QtCore
from src.components.player.PlayerController import PlayerController


class Player(QtWidgets.QWidget):

    @property
    def controller(self):
        return self._controller

    @property
    def context(self):
        return self._context

    def __init__(self, context, *args):
        super(Player, self).__init__(*args)
        self._controller = PlayerController(self, context)
        self._context = context

        self.setup_ui()
        self.retranslate_ui()
        self.create_connections()
        self.context.player = self

    def setup_ui(self):
        self.setMinimumSize(QtCore.QSize(790, 45))
        self.h_layout = QtWidgets.QHBoxLayout(self)

        self.prev_button = QtWidgets.QPushButton(self)
        self.prev_button.setEnabled(False)
        self.prev_button.setMaximumWidth(30)

        self.play_pause_button = QtWidgets.QPushButton(self)
        self.play_pause_button.setEnabled(False)
        self.play_pause_button.setMaximumWidth(30)

        self.next_button = QtWidgets.QPushButton(self)
        self.next_button.setEnabled(False)
        self.next_button.setMaximumWidth(30)

        self.h_layout.addWidget(self.prev_button)
        self.h_layout.addWidget(self.play_pause_button)
        self.h_layout.addWidget(self.next_button)

        self.h_slider = QtWidgets.QSlider(self)
        self.h_slider.setOrientation(QtCore.Qt.Horizontal)
        self.h_layout.addWidget(self.h_slider)
        self.progress_bar = QtWidgets.QProgressBar(self)
        self.progress_bar.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.h_layout.addWidget(self.progress_bar)
        self.h_layout.setStretch(3, 16)
        self.h_layout.setStretch(4, 80)

    def retranslate_ui(self):
        self.play_pause_button.setText('▶')
        self.prev_button.setText('⏪')
        self.next_button.setText('⏩')

    def create_connections(self):
        app = self._context.app
        app.DZ_PLAYER_EVENT_QUEUELIST_LOADED.connect(self.controller.on_track_content_loaded)
        app.DZ_PLAYER_EVENT_RENDER_TRACK_START.connect(self.controller.on_track_play_start)

        app.DZ_PLAYER_EVENT_RENDER_TRACK_PAUSED.connect(self.controller.on_track_pause)
        app.DZ_PLAYER_EVENT_LIMITATION_FORCED_PAUSE.connect(self.controller.on_track_pause)
        app.DZ_PLAYER_EVENT_RENDER_TRACK_RESUMED.connect(self.controller.on_track_resume)
        self.play_pause_button.clicked.connect(self.controller.on_play_pause_click)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = Player()
    widget.show()
    sys.exit(app.exec_())
