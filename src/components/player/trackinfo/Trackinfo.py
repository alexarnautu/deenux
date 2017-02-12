from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QTimer

from src.components.View import View
from src.components.player.trackinfo.TrackinfoController import TrackinfoController


class Trackinfo(QtWidgets.QWidget, View):

    def __init__(self, context, *args):
        QtWidgets.QWidget.__init__(self, *args)
        View.__init__(self, context, TrackinfoController(self, context))

        self.pbar_timer = QTimer()
        self.pbar_timer.setInterval(100)  # 1/10 seconds, 1000 milliseconds

        self.setup()

    def setup_ui(self):
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

    def retranslate_ui(self):
        pass

    def create_connections(self):
        ctrl = self.controller
        self.progress_bar.sliderPressed.connect(ctrl.on_progress_bar_pressed)
        self.progress_bar.sliderReleased.connect(ctrl.on_progress_bar_released)
        self.progress_bar.valueChanged.connect(ctrl.on_progress_bar_value_changed)

        self.pbar_timer.timeout.connect(ctrl.update_progress_bar)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = Trackinfo({})
    widget.show()
    sys.exit(app.exec_())
