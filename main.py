import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow

from PyQt5.QtCore import Qt


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.round = []
        self.pushButton.clicked.connect(self.change)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(QPen(Qt.yellow, 8, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        for i in range(len(self.round)):
            painter.drawEllipse(self.round[i][0], self.round[i][1], self.round[i][2], self.round[i][2])
        painter.end()

    def change(self):
        self.round.append((randint(10, 990), randint(50, 350), randint(10, 50)))
        self.update()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())