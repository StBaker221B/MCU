
from PyQt5 import QtWidgets, QtCore
from mainwindow import Ui_MainWindow
import sys

from PyQt5.QtCore import QTimer
import serial
import myslot
import scom

from PyQt5.QtCore import QThread, pyqtSignal
# from QThread_Example_UI import Ui_Form

# class mainwindow(QtWidgets.QMainWindow, Ui_Form):
class mainwindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mainwindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ser = scom.spopen()
        if(ser == 0):
            print("fail")
        else:
            self.ui.button_C_0.clicked.connect(
                lambda : myslot.btn_C_0_clicked(ser, self.ui.button_C_0.isChecked()))
            self.ui.button_C_1.clicked.connect(
                lambda : myslot.btn_C_1_clicked(ser, self.ui.button_C_1.isChecked()))
        # self.ui.button_C_2.clicked.connect(myslot.btn_C_2_clicked(ser))
        # self.ui.button_C_3.clicked.connect(myslot.btn_C_3_clicked(ser))
        # self.ui.button_C_4.clicked.connect(myslot.btn_C_4_clicked(ser))
        # self.ui.button_C_5.clicked.connect(myslot.btn_C_5_clicked(ser))
        # self.ui.button_C_6.clicked.connect(myslot.btn_C_6_clicked(ser))
        # self.ui.button_C_7.clicked.connect(myslot.btn_C_7_clicked(ser))
        # self.ui.button_C_8.clicked.connect(myslot.btn_C_8_clicked(ser))
        # self.ui.button_C_9.clicked.connect(myslot.btn_C_9_clicked(ser))
        
        # self.timer = QTimer(self)
        # self.timer.timeout.connect(lambda : self.update(ser)) 
        # self.timer.start(100)
        # self.update(ser)

        self.update = updateThread(ser)
        self.update.start()
        self.update.trigger.connect(self.updateSwitch)
        
        self.switchTable = {
            "C":[self.ui.button_C_0, self.ui.button_C_1, 
            self.ui.button_C_2, self.ui.button_C_3, 
            self.ui.button_C_4, self.ui.button_C_5,
            self.ui.button_C_6, self.ui.button_C_7,
            self.ui.button_C_8, self.ui.button_C_9]}

    # def update(self, ser):
    #     data = ser.read(10)
    #     if data != b'':
    #         print('receive data is :', data)
        # QtWidgets.QApplication.processEvents()

    def updateSwitch(self, report):
        print(report)
        portNum = int(report[1])
        portState = int(report[2])
        switch = self.switchTable[report[0]][portNum]
        print(switch.isChecked())
        if(report[2] == '0'):
            if(not switch.isChecked()):
                switch.toggle()
        if(report[2] == '1'):
            if(switch.isChecked()):
                switch.toggle()

        # if(switch.isChecked()):
        #     if(report[2] == '1'):
        #         switch.toggle()
        # if(~switch.isChecked()):
        #     if(report[2] == '0'):
        #         switch.toggle()

class updateThread(QThread):
    trigger = pyqtSignal(str)

    def __init__(self, ser):
        super(updateThread, self).__init__()
        self.ser = ser

    def run(self):
        while True:
            data = self.ser.read(3)
            if data != b'':
                # data = list(data)
                data = bytes.decode(data)
                # data = data[2:5]
                # print(data)
                self.trigger.emit(data)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = mainwindow()
    window.show()
    # ser = scom.spopen()
    # status = app.exec_()
    sys.exit(app.exec_())
    # print(status)

    # sys.exit(status)