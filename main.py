import sys
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine, QQmlContext
from PyQt5.QtCore import pyqtProperty, QObject

class People(QObject):

    _name = "Felipe gatinho do Bio"

    @pyqtProperty('QString')
    def name(self):
        self._name = "end"
        return self._name

    # Define the setter of the 'name' property.
    @name.setter
    def name(self, name):
        self._name = name

    def __init__(self, parent  = None):
        super(QObject, self).__init__(parent)


app = QApplication(sys.argv)

felipe = People()

engine = QQmlApplicationEngine("main.qml")
ctx = engine.rootContext()

ctx.setContextProperty("felipe", felipe)

sys.exit(app.exec_())
