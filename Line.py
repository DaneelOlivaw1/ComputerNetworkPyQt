from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import Point


class Line(QWidget):
    def __init__(self, a: Point, b: Point):
        super(Line, self).__init__(None)
        self.a = a
        self.b = b


    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawline(qp)
        qp.end()

    def drawline(self, qp: QPainter):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.a.x, self.a.y, self.b.x, self.b.y)
