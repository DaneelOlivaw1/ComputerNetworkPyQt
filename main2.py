import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Computer import Computer
from control import ControlWidget
from NetworkWidget import NetworkWidget
from LinesWidget import LinesWidget
 
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.resize(1000, 600)
        self.status = self.statusBar()
        self.status.showMessage("10000", 5000)
        self.setWindowTitle("计算机网络课设")


        self.initUI()
        self.center()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        # self.move(screen.width() - size.width() / 2, screen.height() - screen.height() / 2)

    def initUI(self):
        w = QWidget()  # MainWindow内的Weight
        controlweight = ControlWidget()  # controlWeight
        networkweight = NetworkWidget() # networkweight
        lineswidget = LinesWidget()
        vlines, hlines = networkweight.getlines()
        lineswidget.init(vlines, hlines)
        lineswidget.show()
        vbox = QVBoxLayout()  # 垂直布局
        vbox.addStretch(1)
        vbox.addWidget(lineswidget)
        vbox.addLayout(networkweight.getlayout())
        vbox.addStretch(1)
        vbox.addLayout(controlweight.getlayout())

        w.setLayout(vbox)
        self.setCentralWidget(w)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())