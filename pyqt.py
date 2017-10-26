import sys
from PyQt5.QtCore import (Qt, QTimer, QTime)
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
    QVBoxLayout, QApplication, QLabel, QGridLayout, QGroupBox)
from PyQt5.QtGui import QIcon, QPixmap

from client import Client

class Display(QLCDNumber):

    def __init__(self):
        super(Display, self).__init__()
        self.title = 'Weather Station'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
        #self.setWindowTitle("digital clock")
        #self.timer = QTimer()
        #self.timer.timeout.connect(self._update)
        #self.timer.start(1000)

        #self.client = Client()

    def contentBlock(self):
        label = QLabel(self)
        pixmap = QPixmap('thermometer.png')
        label.setPixmap(pixmap)
        label.move(10, 10)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.contentBlock()

        self.show()



    def _update(self):
        dataStream = self.client.getData()
        global counter
        counter += 1
        self.display(dataStream[1])


def main():
    app = QApplication([])
    w = Display()
    #w.show()
    #w.resize(300, 100)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()