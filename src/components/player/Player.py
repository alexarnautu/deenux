
from PyQt5 import QtWidgets, QtCore
from src.components.player.PlayerController import PlayerController


class Player(QtWidgets.QWidget):

    @property
    def controller(self):
        return self._controller

    def __init__(self, *args):
        super(Player, self).__init__(*(args[1:]))
        self._controller = PlayerController(self, args[0])
        self._context = args[0]

        self.setup_ui()
        self.retranslate_ui()
        self.create_connections()

    def setup_ui(self):
        self.setMinimumSize(QtCore.QSize(790, 45))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.playStopButton = QtWidgets.QPushButton(self)
        self.playStopButton.setMinimumSize(QtCore.QSize(0, 27))
        self.playStopButton.setObjectName("playStopButton")
        self.horizontalLayout.addWidget(self.playStopButton)
        self.horizontalSlider = QtWidgets.QSlider(self)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout.addWidget(self.horizontalSlider)
        self.progress_bar = QtWidgets.QProgressBar(self)
        self.progress_bar.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.progress_bar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progress_bar)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 16)
        self.horizontalLayout.setStretch(2, 80)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.playStopButton.setText(_translate("Form", "Play"))

    def create_connections(self):
        self._context.deezer.jukebox.on('DZ_PLAYER_EVENT_QUEUELIST_LOADED', self.controller.on_track_content_loaded)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = Player()
    widget.show()
    sys.exit(app.exec_())
