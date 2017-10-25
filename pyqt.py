import sys
from PyQt5.QtCore import (Qt, QTimer, QTime)
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
    QVBoxLayout, QApplication)

from client import Client

counter = 0

class Display(QLCDNumber):

    def __init__(self):
        super(Display, self).__init__()
        self.setWindowTitle("digital clock")
        self.timer = QTimer()
        self.timer.timeout.connect(self._update)
        self.timer.start(1000)

        self.client = Client()

    def _update(self):
        dataStream = self.client.getData()
        global counter
        counter += 1
        self.display(dataStream[1])



def main():
    app = QApplication([])
    w = Display()
    w.show()
    w.resize(300, 100)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()