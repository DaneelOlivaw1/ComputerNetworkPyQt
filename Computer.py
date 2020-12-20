from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import random

class Computer(QWidget):

    def __init__(self, IP, widget:QWidget):
        super(Computer, self).__init__(None)
        # 设置图片
        self.IP = IP
        self.widget = widget
        self.MAC = self.generateMAC()
        self.setpic()




    def setpic(self):

        lenth = 50
        computer_pic = QPixmap("Computer.png").scaledToHeight(lenth)
        vbox = QVBoxLayout()

        computerlabel = QLabel()
        computerlabel.setAlignment(Qt.AlignCenter)
        computerlabel.setPixmap(computer_pic)

        self.computerbtn = QPushButton("编辑")
        # computerbtn.setCheckable(True)
        self.child = childwindow()
        self.child.setipmac(self)
        self.computerbtn.clicked.connect(self.link_clicked)

        vbox.addWidget(computerlabel)
        vbox.addWidget(self.computerbtn)
        self.computerlayout = vbox


    def generateMAC(self):
        mmax = 238
        mmin = 0
        res = ""
        for i in range(6):
            tmp = random.randint(mmin, mmax)
            tmp = str(hex(tmp))[2:]
            if (len(tmp) == 1):
                tmp = '0' + tmp

            if (i != 0):
                res += '-'
            res += str(tmp)
        print(res)
        return res

    def getcomputerlayout(self):
        return self.computerlayout

    def link_clicked(self):
        self.child.show()



class childwindow(QWidget):
    def __init__(self, parent=None):
        super(childwindow, self).__init__(parent)
        self.setFixedWidth(500)
        self.setFixedHeight(300)
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        ip_label = QLabel("IP:")
        self.ip_input = QLineEdit()
        vbox.addWidget(ip_label)
        vbox.addWidget(self.ip_input)
        mac_label = QLabel("MAC:")
        self.mac_input = QLineEdit()
        vbox.addWidget(mac_label)
        vbox.addWidget(self.mac_input)

        okButton = QPushButton("OK")
        okButton.clicked.connect(self.clickOK)
        cancelButton = QPushButton("Cancel")
        cancelButton.clicked.connect(self.close)
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def setipmac(self, c:Computer):
        self.ip_input.setText(c.IP)
        self.mac_input.setText(c.MAC)

        self.computer = c

    def clickOK(self):
        self.computer.IP = self.ip_input.text()
        self.computer.MAC = self.mac_input.text()

        self.close()

