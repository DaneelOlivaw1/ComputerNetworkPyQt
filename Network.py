from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Computer import Computer
from Line import Line
from Point import Point


class NetWork:

    def __init__(self, num: int, widget:QWidget):
        self.computers = []
        root_ip = "192.168.0."
        for i in range(max(num, 7)):
            c = Computer(root_ip + str(i), widget)
            self.computers.append(c)

    def getcomputers(self):
        return self.computers

    def getlines(self):
        vlines = []
        for i in self.computers:
            a = Point(i.x() - i.width() / 2, i.y())
            b = Point(i.x() - i.width() / 2, i.y() - 10)
            line = Line(a, b)
            vlines.append(line)

        hlines = []
        for i in range(len(self.computers) - 1):
            a = Point(self.computers[i].x() - self.computers[i].width() / 2,
                      self.computers[i].y() - 10)
            b = Point(self.computers[i+1].x() - self.computers[i+1].width() / 2,
                      self.computers[i+1].y() - 10)
            line = Line(a, b)
            hlines.append(line)

        return vlines, hlines






