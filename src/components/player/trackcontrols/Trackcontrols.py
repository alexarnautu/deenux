from PyQt5 import QtWidgets, QtCore

from src.components.View import View
from src.components.player.trackcontrols.TrackcontrolsController import TrackcontrolsController


class Trackcontrols(QtWidgets.QWidget, View):

    def __init__(self, context, *args):
        QtWidgets.QWidget.__init__(self, *args)
        View.__init__(self, context, TrackcontrolsController(self, context))
        self.setup()

    def setup_ui(self):
        
        layout = QtWidgets.QHBoxLayout(self)
        l1 = QtWidgets.QHBoxLayout()
        l2 = QtWidgets.QHBoxLayout()
        l3 = QtWidgets.QVBoxLayout()

        self.prev_button = QtWidgets.QPushButton(self)
        self.prev_button.setEnabled(False)
        self.prev_button.setMaximumWidth(30)

        self.play_pause_button = QtWidgets.QPushButton(self)
        self.play_pause_button.setEnabled(False)
        self.play_pause_button.setMaximumWidth(30)

        self.next_button = QtWidgets.QPushButton(self)
        self.next_button.setEnabled(False)
        self.next_button.setMaximumWidth(30)

        self.volume_slider = QtWidgets.QSlider(self)
        self.volume_slider.setOrientation(QtCore.Qt.Horizontal)
        self.volume_slider.setMaximum(15)

        self.shuffle_button = QtWidgets.QPushButton(self)
        self.shuffle_button.setMaximumWidth(30)
        self.repeat_button = QtWidgets.QPushButton(self)
        self.repeat_button.setMaximumWidth(30)

        l3.addLayout(l1)
        l3.addLayout(l2)

        l1.addWidget(self.prev_button)
        l1.addWidget(self.play_pause_button)
        l1.addWidget(self.next_button)

        l2.addWidget(self.shuffle_button)
        l2.addWidget(self.repeat_button)

        layout.addLayout(l3)
        layout.addWidget(self.volume_slider, 16)

    def retranslate_ui(self):
        self.play_pause_button.setText('▶')
        self.prev_button.setText('⏪')
        self.next_button.setText('⏩')
        self.shuffle_button.setText('sh')

    def create_connections(self):
        ctrl = self.controller
        app = self.context.app

        self.volume_slider.valueChanged.connect(ctrl.on_volume_change)
        self.play_pause_button.clicked.connect(ctrl.on_play_pause_click)
        self.shuffle_button.clicked.connect(ctrl.on_shuffle_click)
        self.next_button.clicked.connect(ctrl.on_next_clicked)
        self.prev_button.clicked.connect(ctrl.on_prev_clicked)

        app.DZ_PLAYER_EVENT_RENDER_TRACK_END.connect(ctrl.on_track_stop)
        app.DZ_PLAYER_EVENT_RENDER_TRACK_START.connect(ctrl.on_track_play_start)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = Trackcontrols({})
    widget.show()
    sys.exit(app.exec_())
