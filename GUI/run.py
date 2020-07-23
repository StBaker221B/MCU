
from Controller import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

# from mylog import LogAssistant

# import SPtest
from SPtest import com
import serial


class Control_window(QtWidgets.QMainWindow ):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.pushButton.clicked.connect(self.query_formula)
        # 给button 的 点击动作绑定一个事件处理函数

        self.ui.SwitchBtn_1.clicked.connect(self.act_1)
        # self.SwitchBtn_2.clicked.connect(self.labelState_2.clear)
        self.ui.SwitchBtn_2.clicked.connect(self.act_2)
        # self.SwitchBtn_3.clicked.connect(self.labelState_3.clear)
        self.ui.SwitchBtn_3.clicked.connect(self.act_3)


    # def query_formula(self):
        # 此处编写具体的业务逻辑

    def act_1(self):
        label = self.ui.labelState_1.text()
        if (label == "OFF"):
            self.ui.labelState_1.setText("ON")
            com(b'1\r\n')
        else:
            self.ui.labelState_1.setText("OFF")
            com(b'0\r\n')

    def act_2(self):
        label = self.ui.labelState_2.text()
        if (label == "OFF"):
            self.ui.labelState_2.setText("ON")
            com(b'1\r\n')
        else:
            self.ui.labelState_2.setText("OFF")
            com(b'0\r\n')

    def act_3(self):
        label = self.ui.labelState_3.text()
        if (label == "OFF"):
            self.ui.labelState_3.setText("ON")
        else:
            self.ui.labelState_3.setText("OFF")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Control_window()
    window.show()
    sys.exit(app.exec_())

