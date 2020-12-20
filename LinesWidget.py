from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class LinesWidget(QWidget):
    def __init__(self):
        super(LinesWidget, self).__init__(None)


    def init(self, vlines, hlines):
        self.vlines = vlines
        self.hlines = hlines

    def paintEvent(self, QPaintEvent):
        qp = QPainter()
        qp.begin(self)
        self.drawlines(qp)
        qp.end()

    def drawlines(self, qp: QPainter):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        qp.setPen(pen)
        for i in self.vlines:
            qp.drawLine(i.a.x, i.a.y, i.b.x, i.b.y)
        for i in self.hlines:
            qp.drawLine(i.a.x, i.a.y, i.b.x, i.b.y)

