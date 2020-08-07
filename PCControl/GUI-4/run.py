
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
            # PSA 1
            self.ui.BTN_PSA1_IN.clicked.connect(
                lambda : myslot.BTN_PSA1_IN_clicked(ser, self.ui.BTN_PSA1_IN.isChecked()))
            self.ui.BTN_PSA1_PRO.clicked.connect(
                lambda : myslot.BTN_PSA1_PRO_clicked(ser, self.ui.BTN_PSA1_PRO.isChecked()))
            self.ui.BTN_PSA1_BAL.clicked.connect(
                lambda : myslot.BTN_PSA1_BAL_clicked(ser, self.ui.BTN_PSA1_BAL.isChecked()))
            self.ui.BTN_PSA1_CLR.clicked.connect(
                lambda : myslot.BTN_PSA1_CLR_clicked(ser, self.ui.BTN_PSA1_CLR.isChecked()))
            # PSA 2
            self.ui.BTN_PSA2_IN.clicked.connect(
                lambda : myslot.BTN_PSA2_IN_clicked(ser, self.ui.BTN_PSA2_IN.isChecked()))
            self.ui.BTN_PSA2_PRO.clicked.connect(
                lambda : myslot.BTN_PSA2_PRO_clicked(ser, self.ui.BTN_PSA2_PRO.isChecked()))
            self.ui.BTN_PSA2_BAL.clicked.connect(
                lambda : myslot.BTN_PSA2_BAL_clicked(ser, self.ui.BTN_PSA2_BAL.isChecked()))
            self.ui.BTN_PSA2_CLR.clicked.connect(
                lambda : myslot.BTN_PSA2_CLR_clicked(ser, self.ui.BTN_PSA2_CLR.isChecked()))
            # PROD 
            self.ui.BTN_PROD_OUT.clicked.connect(
                lambda : myslot.BTN_PROD_OUT_clicked(ser, self.ui.BTN_PROD_OUT.isChecked()))
            self.ui.BTN_PROD_PSA1.clicked.connect(
                lambda : myslot.BTN_PROD_PSA1_clicked(ser, self.ui.BTN_PROD_PSA1.isChecked()))
            self.ui.BTN_PROD_PSA2.clicked.connect(
                lambda : myslot.BTN_PROD_PSA2_clicked(ser, self.ui.BTN_PROD_PSA2.isChecked()))
            # COL2
            self.ui.BTN_COL2_IN.clicked.connect(
                lambda : myslot.BTN_COL2_IN_clicked(ser, self.ui.BTN_COL2_IN.isChecked()))
     
        self.ui.actionStart.triggered.connect(lambda : myslot.setAutostart(ser))
        self.ui.actionRepeat.triggered.connect(lambda : myslot.setAutorepeat(ser))
        self.ui.actionManual.triggered.connect(lambda : myslot.setMaunal(ser))
        # self.ui.actionAbout.triggered.connect()

        # self.ui.button_C_2.clicked.connect(myslot.btn_C_2_clicked(ser))
        
        # self.timer = QTimer(self)
        # self.timer.timeout.connect(lambda : self.update(ser)) 
        # self.timer.start(100)
        # self.update(ser)

        self.update = updateThread(ser)
        self.update.start()
        self.update.trigger.connect(self.updateSwitch)
        
        # self.switchTable = {
        #     "C":[self.ui.button_C_0, self.ui.button_C_1, 
        #     self.ui.button_C_2, self.ui.button_C_3, 
        #     self.ui.button_C_4, self.ui.button_C_5,
        #     self.ui.button_C_6, self.ui.button_C_7,
        #     self.ui.button_C_8, self.ui.button_C_9]}
        self.switchTable = {
            "PSA1":[self.ui.BTN_PSA1_IN, self.ui.BTN_PSA1_PRO, 
            self.ui.BTN_PSA1_BAL, self.ui.BTN_PSA1_CLR],
            "PSA2":[self.ui.BTN_PSA2_IN, self.ui.BTN_PSA2_PRO,
            self.ui.BTN_PSA2_BAL, self.ui.BTN_PSA2_CLR],
            "PROD":[self.ui.BTN_PROD_OUT, self.ui.BTN_PROD_PSA1,
            self.ui.BTN_PROD_PSA2],
            "COL2":[self.ui.BTN_COL2_IN]}

    # def update(self, ser):
    #     data = ser.read(10)
    #     if data != b'':
    #         print('receive data is :', data)
        # QtWidgets.QApplication.processEvents()

    def updateSwitch(self, report):
        # print(report)
        report = report.split()
        print(report)
        section = report[0]
        function = report[1]
        # portState = int(report[2])
        # switch = self.switchTable[report[0]][portNum]
        if(section == 'PSA1' or section == 'PSA2'):
            if(function == 'IN'):
                switch = self.switchTable[section][0]
            elif(function == 'PRO'):
                switch = self.switchTable[section][1]
            elif(function == 'BAL'):
                switch = self.switchTable[section][2]
            elif(function == 'CLR'):
                switch = self.switchTable[section][3]
        elif(section == 'PROD'):
            if(function == 'OUT'):
                switch = self.switchTable[section][0]
            elif(function == 'PSA1'):
                switch = self.switchTable[section][1]
            elif(function == 'PSA2'):
                switch = self.switchTable[section][2]
        elif(section == 'COL2'):
            if(function == 'IN'):
                switch = self.switchTable['COL2'][0]
                
        print(switch.isChecked())
        if(report[2] == '1'):
            if(not switch.isChecked()):
                switch.toggle()
        if(report[2] == '0'):
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
            data = self.ser.read(11)
            # if data != b'':
            if data != 0x00:
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