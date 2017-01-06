from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import QObject, QUrl
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQuick import QQuickView
from PyQt5.QtQml import qmlRegisterType, QQmlComponent, QQmlEngine, QQmlApplicationEngine
import sys


def button_handler():
    print("You clicked me")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    ctx = engine.rootContext()
    engine.load(QUrl('../views/hello_world.qml'))

    window = engine.rootObjects()[0]

    button = window.findChild(QObject, 'hello_button')
    button.handler.connect(button_handler)

    window.show()

    sys.exit(app.exec_())






