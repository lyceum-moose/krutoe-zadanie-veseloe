import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import random


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.must_draw = False

    def run(self):
        self.pushButton.setEnabled(False)
        self.must_draw = True
        self.repaint()

    def paintEvent(self, event):
        if self.must_draw:
            painter = QtGui.QPainter()
            painter.begin()
            pen = QtGui.QPen()
            pen.setWidth(5)
            painter.setPen(pen)
            qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            for i in range(10):
                painter.drawEllipse(random.randint(100, 600), random.randint(100, 600), 70, 70)
            painter.end()
            self.must_draw = False
            self.pushButton.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
