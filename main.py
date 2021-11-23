from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from random import randrange
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(500, 400)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(150, 10, 131, 41))

        self.retranslateUi()

    def retranslateUi(self):
        self.setWindowTitle("MainWindow")
        self.pushButton.setText("Круг")
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw(self, qp):
        x, y, ran = randrange(300), randrange(200), randrange(200)
        r, g, b = randrange(255), randrange(255), randrange(255)
        qp.setBrush(QColor(r, g, b))
        qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
