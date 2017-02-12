
from PyQt5 import QtWidgets, QtCore

from src.components.View import View
from src.components.sidemenu.SidemenuController import SidemenuController


class Sidemenu(QtWidgets.QWidget, View):

    def __init__(self, context, *args):
        QtWidgets.QWidget.__init__(self, *args)
        View.__init__(self, context, SidemenuController(self, context))
        self.setup()

    def setup_ui(self):
        self.setMinimumSize(QtCore.QSize(40, 0))

    def retranslate_ui(self):
        pass

    def create_connections(self):
        pass

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = Sidemenu()
    widget.show()
    sys.exit(app.exec_())
