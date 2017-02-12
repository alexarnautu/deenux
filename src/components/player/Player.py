
from PyQt5 import QtWidgets, QtCore

from src.components.View import View
from src.components.player.PlayerController import PlayerController


class Player(QtWidgets.QWidget, View):

    def __init__(self, context, *args):
        QtWidgets.QWidget.__init__(self, *args)
        View.__init__(self, context, PlayerController(self, context))
        self.setup()

        self.context.player = self
        self.active = False

    def setup_ui(self):
        self.setMinimumSize(QtCore.QSize(790, 60))
        h_layout = QtWidgets.QHBoxLayout(self)

        self.prev_button = QtWidgets.QPushButton(self)
        self.prev_button.setEnabled(False)
        self.prev_button.setMaximumWidth(30)

        self.play_pause_button = QtWidgets.QPushButton(self)
        self.play_pause_button.setEnabled(False)
        self.play_pause_button.setMaximumWidth(30)

        self.next_button = QtWidgets.QPushButton(self)
        self.next_button.setEnabled(False)
        self.next_button.setMaximumWidth(30)

        h_layout.addWidget(self.prev_button)
        h_layout.addWidget(self.play_pause_button)
        h_layout.addWidget(self.next_button)

        self.volume_slider = QtWidgets.QSlider(self)
        self.volume_slider.setOrientation(QtCore.Qt.Horizontal)
        self.volume_slider.setMaximum(15)

        h_layout.addWidget(self.volume_slider, 16)

        label_layout = QtWidgets.QHBoxLayout()
        self.playing_label = QtWidgets.QLabel(self)
        self.time_label = QtWidgets.QLabel(self)
        label_layout.addWidget(self.playing_label, 1)
        label_layout.addWidget(self.time_label)

        self.progress_bar = QtWidgets.QSlider(self)
        self.progress_bar.setOrientation(QtCore.Qt.Horizontal)

        h_progress_layout = QtWidgets.QVBoxLayout(self)
        h_progress_layout.addLayout(label_layout)
        h_progress_layout.addWidget(self.progress_bar)
        h_layout.addLayout(h_progress_layout, 80)
        h_layout.insertSpacing(4, 10)

    def retranslate_ui(self):
        self.play_pause_button.setText('▶')
        self.prev_button.setText('⏪')
        self.next_button.setText('⏩')

    def create_connections(self):
        app = self.context.app
        ctrl = self.controller
        app.DZ_PLAYER_EVENT_QUEUELIST_LOADED.connect(ctrl.on_track_content_loaded)
        app.DZ_PLAYER_EVENT_RENDER_TRACK_START.connect(ctrl.on_track_play_start)

        app.DZ_PLAYER_EVENT_RENDER_TRACK_PAUSED.connect(ctrl.on_track_pause)
        app.DZ_PLAYER_EVENT_LIMITATION_FORCED_PAUSE.connect(ctrl.on_track_pause)
        app.DZ_PLAYER_EVENT_RENDER_TRACK_RESUMED.connect(ctrl.on_track_resume)
        app.DZ_PLAYER_EVENT_RENDER_TRACK_END.connect(ctrl.on_track_stop)

        self.volume_slider.valueChanged.connect(ctrl.on_volume_change)
        self.play_pause_button.clicked.connect(ctrl.on_play_pause_click)
        self.next_button.clicked.connect(ctrl.on_next_clicked)
        self.prev_button.clicked.connect(ctrl.on_prev_clicked)

        self.progress_bar.sliderPressed.connect(ctrl.on_progress_bar_pressed)
        self.progress_bar.sliderReleased.connect(ctrl.on_progress_bar_released)
        self.progress_bar.valueChanged.connect(ctrl.on_progress_bar_value_changed)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = Player()
    widget.show()
    sys.exit(app.exec_())
