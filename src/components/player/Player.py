
from PyQt5 import uic, QtWidgets
from src.components.player.PlayerController import PlayerController
import os


class Player(QtWidgets.QWidget):

    def create_connections(self):
        pass

    @property
    def controller(self):
        return self._controller

    def __init__(self, *args):
        super(Player, self).__init__(*(args[1:]))
        self._controller = PlayerController(args[0])
        uic.loadUi(os.path.realpath(os.path.dirname(__file__)) + '/Player.ui', self)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = Player()
    widget.show()
    sys.exit(app.exec_())
