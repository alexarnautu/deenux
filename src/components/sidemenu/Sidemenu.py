
from PyQt5 import QtWidgets, QtCore
from src.components.sidemenu.SidemenuController import SidemenuController


class Sidemenu(QtWidgets.QWidget):

    @property
    def controller(self):
        return self._controller

    def __init__(self, context, *args):
        super(Sidemenu, self).__init__(*args)
        self._controller = SidemenuController(self, context)

        self.setup_ui()
        self.retranslate_ui()
        self.create_connections()

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
