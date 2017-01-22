
from PyQt5 import uic, QtWidgets
from src.components.player.PlayerController import PlayerController

class Player(QtWidgets.QWidget):

    def createConnections(self):
        pass

    @property
    def controller(self):
        return self._controller

    def __init__(self, context, *args):
        super(Player, self).__init__(*args)
        self._controller = PlayerController(context)
        uic.loadUi('player.ui', self)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = Player()
    widget.show()
    sys.exit(app.exec_())
