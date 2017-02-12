from PyQt5 import QtWidgets, QtCore

from src.components.View import View
from src.components.player.trackcontrols.TrackcontrolsController import TrackcontrolsController


class Trackcontrols(QtWidgets.QWidget, View):

    def __init__(self, context, *args):
        QtWidgets.QWidget.__init__(self, *args)
        View.__init__(self, context, TrackcontrolsController(self, context))
        self.setup()

    def setup_ui(self):
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

    def retranslate_ui(self):
        self.play_pause_button.setText('▶')
        self.prev_button.setText('⏪')
        self.next_button.setText('⏩')

    def create_connections(self):
        ctrl = self.controller

        self.volume_slider.valueChanged.connect(ctrl.on_volume_change)
        self.play_pause_button.clicked.connect(ctrl.on_play_pause_click)
        self.next_button.clicked.connect(ctrl.on_next_clicked)
        self.prev_button.clicked.connect(ctrl.on_prev_clicked)

        self.context.app.DZ_PLAYER_EVENT_RENDER_TRACK_END.connect(ctrl.on_track_stop)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = Trackcontrols({})
    widget.show()
    sys.exit(app.exec_())
