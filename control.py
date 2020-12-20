from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class ControlWidget(QWidget):
    def __init__(self):
        super(ControlWidget, self).__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        hbox = QHBoxLayout()
        hhbox = QHBoxLayout()
        from_label = QLabel("从：")
        from_combobox = QComboBox()

        hhbox.addWidget(from_label)
        hhbox.addWidget(from_combobox)
        hhbox.setSpacing(0)
        hbox.addLayout(hhbox)
        hhbox = QHBoxLayout()
        to_label = QLabel("到：")
        to_combobox = QComboBox()
        hhbox.addWidget(to_label)
        hhbox.addWidget(to_combobox)
        hhbox.setSpacing(0)
        hhbox.addStretch(1)
        hbox.addLayout(hhbox)
        vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        data_label = QLabel("数据：")
        data_input = QLineEdit()
        hbox.addWidget(data_label)
        hbox.addWidget(data_input)
        hbox.addStretch(1)
        vbox.addLayout(hbox)

        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        vbox.addLayout(hbox)


        self.vbox = vbox

    def getlayout(self):
        return self.vbox

    def okdeal():
        print("Hello")