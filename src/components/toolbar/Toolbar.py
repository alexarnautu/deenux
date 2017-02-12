
from PyQt5 import QtWidgets, QtCore

from src.components.View import View
from src.components.toolbar.ToolbarController import ToolbarController


class Toolbar(QtWidgets.QWidget, View):

    def __init__(self, context, *args):
        super(Toolbar, self).__init__(*args)
        self._controller = ToolbarController(self, context)
        self._context = context

        self.setup_ui()
        self.retranslate_ui()
        self.create_connections()

    def setup_ui(self):
        self.setMinimumSize(QtCore.QSize(0, 40))

    def retranslate_ui(self):
        pass

    def create_connections(self):
        pass

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = Toolbar()
    widget.show()
    sys.exit(app.exec_())
