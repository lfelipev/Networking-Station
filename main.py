import sys
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine, QQmlContext
from PyQt5.QtCore import pyqtProperty, QObject
from client import Client

class People(QObject):

    def __init__(self, parent  = None):
        super(QObject, self).__init__(parent)
        self.value = 0
        self.client = Client()

    @pyqtProperty('QString')
    def name(self):
        dataString = self.client.getData()
        self.value += 2
        self._name = dataString[1]
        return self._name

    # Define the setter of the 'name' property.
    @name.setter
    def name(self, name):
        self._name = name


def main():
    app = QApplication(sys.argv)
    felipe = People()
    engine = QQmlApplicationEngine("main.qml")
    ctx = engine.rootContext()
    ctx.setContextProperty("felipe", felipe)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


