
from PyQt5 import QtWidgets, QtCore
from src.components.player.PlayerController import PlayerController


class Player(QtWidgets.QWidget):

    def create_connections(self):
        pass

    @property
    def controller(self):
        return self._controller

    def __init__(self, *args):
        super(Player, self).__init__(*(args[1:]))
        self._controller = PlayerController(args[0])
        self.setup_ui()
        self.retranslate_ui()

    def setup_ui(self):
        self.setObjectName("Form")
        self.setMinimumSize(QtCore.QSize(790, 45))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.playStopButton = QtWidgets.QPushButton(self)
        self.playStopButton.setMinimumSize(QtCore.QSize(0, 27))
        self.playStopButton.setObjectName("playStopButton")
        self.horizontalLayout.addWidget(self.playStopButton, 0, QtCore.Qt.AlignRight)
        self.horizontalSlider = QtWidgets.QSlider(self)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout.addWidget(self.horizontalSlider)
        self.progressBar = QtWidgets.QProgressBar(self)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 16)
        self.horizontalLayout.setStretch(2, 80)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.playStopButton.setText(_translate("Form", "Play"))

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = Player()
    widget.show()
    sys.exit(app.exec_())
