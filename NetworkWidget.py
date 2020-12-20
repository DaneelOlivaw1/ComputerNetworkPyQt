from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Network import NetWork


class NetworkWidget(QWidget):
    def __init__(self):
        super(NetworkWidget, self).__init__()
        self.net = NetWork(5, self)


    def getlayout(self):
        computers = self.net.getcomputers()
        hbox = QHBoxLayout()
        for i in computers:
            hbox.addLayout(i.getcomputerlayout())

        return hbox

    def getlines(self):
        return self.net.getlines()