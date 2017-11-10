import sys
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine, QQmlContext
from PyQt5.QtCore import pyqtProperty, QObject
from client import Client

class Status(QObject):

    def __init__(self, parent  = None):
        super(QObject, self).__init__(parent)
        self.temperature = 'Initializing...'
        self.humidity = 'Initializing...'
        self.luminosity = 'Initializing...'
        self.rain = 'Initializing...'
        self.density = 'Initializing...'
        self.client = Client()
        self.dataString = self.client.getData()

    @pyqtProperty('QString')
    def getData(self):
        constant = 'Requesting server data!'
        self.dataString = self.client.getData()
        return constant

    @pyqtProperty('QString')
    def temperature(self):
        self.temperature = self.dataString[0]
        return self._temperature

    @pyqtProperty('QString')
    def humidity(self):
        self.humidity = self.dataString[1]
        return self._humidity

    @pyqtProperty('QString')
    def luminosity(self):
        self.luminosity = self.dataString[2]
        return self._luminosity

    @pyqtProperty('QString')
    def rain(self):
        self.rain = self.dataString[3]
        return self._rain

    @pyqtProperty('QString')
    def density(self):
        self.density = self.dataString[4]
        return self._density


    # Define the setter of the '' property.
    @temperature.setter
    def temperature(self, temperature):
        self._temperature = temperature

    @humidity.setter
    def humidity(self, humidity):
        self._humidity = humidity

    @luminosity.setter
    def luminosity(self, luminosity):
        self._luminosity = luminosity

    @rain.setter
    def rain(self, rain):
        self._rain = rain

    @density.setter
    def density(self, density):
        self._density = density

def main():
    app = QApplication(sys.argv)
    status = Status()
    engine = QQmlApplicationEngine("main.qml")
    ctx = engine.rootContext()
    ctx.setContextProperty("status", status)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


