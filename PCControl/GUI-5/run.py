
from PyQt5 import QtWidgets, QtCore, QtGui
from mainwindow import Ui_MainWindow
from about import Ui_AboutDlg
import sys

from PyQt5.QtCore import QTimer
import serial
import myslot
import scom
import spcom

from PyQt5.QtCore import QThread, pyqtSignal
# from QThread_Example_UI import Ui_Form

# class mainwindow(QtWidgets.QMainWindow, Ui_Form):
class mainwindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mainwindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.aboutDlg = aboutdlg()

        self.ser = scom.spopen()
        if(self.ser == 0):
            print("fail")
        else:
            # PSA 1
            self.ui.BTN_PSA1_IN.clicked.connect(
                lambda : myslot.BTN_PSA1_IN_clicked(self.ser, self.ui.BTN_PSA1_IN.isChecked()))
            self.ui.BTN_PSA1_PRO.clicked.connect(
                lambda : myslot.BTN_PSA1_PRO_clicked(self.ser, self.ui.BTN_PSA1_PRO.isChecked()))
            self.ui.BTN_PSA1_BAL.clicked.connect(
                lambda : myslot.BTN_PSA1_BAL_clicked(self.ser, self.ui.BTN_PSA1_BAL.isChecked()))
            self.ui.BTN_PSA1_CLR.clicked.connect(
                lambda : myslot.BTN_PSA1_CLR_clicked(self.ser, self.ui.BTN_PSA1_CLR.isChecked()))
            # PSA 2
            self.ui.BTN_PSA2_IN.clicked.connect(
                lambda : myslot.BTN_PSA2_IN_clicked(self.ser, self.ui.BTN_PSA2_IN.isChecked()))
            self.ui.BTN_PSA2_PRO.clicked.connect(
                lambda : myslot.BTN_PSA2_PRO_clicked(self.ser, self.ui.BTN_PSA2_PRO.isChecked()))
            self.ui.BTN_PSA2_BAL.clicked.connect(
                lambda : myslot.BTN_PSA2_BAL_clicked(self.ser, self.ui.BTN_PSA2_BAL.isChecked()))
            self.ui.BTN_PSA2_CLR.clicked.connect(
                lambda : myslot.BTN_PSA2_CLR_clicked(self.ser, self.ui.BTN_PSA2_CLR.isChecked()))
            # PROD 
            self.ui.BTN_PROD_OUT.clicked.connect(
                lambda : myslot.BTN_PROD_OUT_clicked(self.ser, self.ui.BTN_PROD_OUT.isChecked()))
            self.ui.BTN_PROD_PSA1.clicked.connect(
                lambda : myslot.BTN_PROD_PSA1_clicked(self.ser, self.ui.BTN_PROD_PSA1.isChecked()))
            self.ui.BTN_PROD_PSA2.clicked.connect(
                lambda : myslot.BTN_PROD_PSA2_clicked(self.ser, self.ui.BTN_PROD_PSA2.isChecked()))
            # COL2
            self.ui.BTN_COL2_IN.clicked.connect(
                lambda : myslot.BTN_COL2_IN_clicked(self.ser, self.ui.BTN_COL2_IN.isChecked()))
     
        self.ui.actionStart.triggered.connect(lambda : myslot.setAutostart(self.ser))
        self.ui.actionRepeat.triggered.connect(lambda : myslot.setAutorepeat(self.ser))
        self.ui.actionManual.triggered.connect(lambda : myslot.setManual(self.ser))
        self.ui.actionRun.triggered.connect(lambda : myslot.setRun(self.ser))
        self.ui.actionPause.triggered.connect(lambda : myslot.setPause(self.ser))
        self.ui.actionAbout.triggered.connect(lambda : self.winAbout())

        self.update = updateThread(self.ser)
        self.update.start()
        self.update.trigger.connect(self.updateState)
        
        self.switchTable = {
            "PSA1":[self.ui.BTN_PSA1_IN, self.ui.BTN_PSA1_PRO, 
            self.ui.BTN_PSA1_BAL, self.ui.BTN_PSA1_CLR],
            "PSA2":[self.ui.BTN_PSA2_IN, self.ui.BTN_PSA2_PRO,
            self.ui.BTN_PSA2_BAL, self.ui.BTN_PSA2_CLR],
            "PROD":[self.ui.BTN_PROD_OUT, self.ui.BTN_PROD_PSA1,
            self.ui.BTN_PROD_PSA2],
            "COL2":[self.ui.BTN_COL2_IN]}

        self.ui.icon_btnOn = QtGui.QIcon(QtGui.QPixmap("./resource/valveon.png"))
        self.ui.icon_btnOff = QtGui.QIcon(QtGui.QPixmap("./resource/valveoff.png"))

        for section in self.switchTable:
            for i in self.switchTable[section]:
                i.setIcon(self.ui.icon_btnOff)

        for i in range(self.ui.table_ValveList.rowCount()):
            item = QtWidgets.QTableWidgetItem("OFF")        
            self.ui.table_ValveList.setItem(i, 0, item)

    def updateState(self, report):
        # print(report)
        report = report.split()
        print(report)
        section = report[1]
        function = report[2]
        if(section[0] == '0' or section[0] == 1
            or section[0] == '\x00'):
            return 
        elif(section == 'TIME'):
            # print(function)
            # self.ui.lcdTIME.display(function)
            time = int(function)/10
            myslot.timeUpdate(time, self.ui)
            return
        elif(section == "CONTROL"):
            myslot.controlUpdate(function, self.ui)
            return 
        # portState = int(report[2])
        # switch = self.switchTable[report[0]][portNum]

        elif(section == 'PSA1' or section == 'PSA2' or 
            section == 'PROD' or section == 'COL2'):
            myslot.valveUpdate(report, self.ui)
        
        # elif(section == 'PSA1' or section == 'PSA2'):
        #     if(function == 'IN'):
        #         switch = self.switchTable[section][0]
        #     elif(function == 'PRO'):
        #         switch = self.switchTable[section][1]
        #     elif(function == 'BAL'):
        #         switch = self.switchTable[section][2]
        #     elif(function == 'CLR'):
        #         switch = self.switchTable[section][3]
        # elif(section == 'PROD'):
        #     if(function == 'OUT'):
        #         switch = self.switchTable[section][0]
        #     elif(function == 'PSA1'):
        #         switch = self.switchTable[section][1]
        #     elif(function == 'PSA2'):
        #         switch = self.switchTable[section][2]
        # elif(section == 'COL2'):
        #     if(function == 'IN'):
        #         switch = self.switchTable[section][0]
                
        # # print(switch.isChecked())
        # if(report[3] == '1'):
        #     if(not switch.isChecked()):
        #         switch.toggle()
        # if(report[3] == '0'):
        #     if(switch.isChecked()):
        #         switch.toggle()

        # # if(switch.isChecked()):
        # #     if(report[2] == '1'):
        # #         switch.toggle()
        # # if(~switch.isChecked()):
        # #     if(report[2] == '0'):
        # #         switch.toggle()
    
    def winAbout(self):
        # self.aboutWin = Ui_AboutDlg()
        self.aboutDlg.show()

class aboutdlg(QtWidgets.QMainWindow):
    def __init__(self):
        super(aboutdlg, self).__init__()
        self.ui = Ui_AboutDlg()
        self.ui.setupUi(self)
        
        self.ui.BTN_OK.clicked.connect(lambda : myslot.BTN_OK_clicked(self))

class updateThread(QThread):
    trigger = pyqtSignal(str)

    def __init__(self, ser):
        super(updateThread, self).__init__()
        self.ser = ser

    # def run(self):
    #     while True:            
    #         data = self.ser.read(11)
    #         print(data)
    #         # print(data[0-8])
    #         if(data != b'' and 
    #             data != b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'):
    #         # if data != 0x00:
    #             # data = list(data)
    #             data = bytes.decode(data)
    #             # data = data.decode('UTF-8', 'strict')
    #             # data = data[2:5]
    #             # print(data)
    #             self.trigger.emit(data)

    def run(self):
        rx = []
        while True:
            if(self.ser.in_waiting):
                rx.append(self.ser.read(1).decode("unicode_escape"))
                l = len(rx)
                if(rx[0] != '*'):
                    if(l == 1):
                        rx = []
                    else:
                        for i in range(l-1):
                            rx[i] = rx[i+1]
                if(l > 3):
                    if(rx[l-1] == '*'):
                        message = ''.join(rx)
                        # print(message)
                        self.trigger.emit(message)
                        rx = []

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = mainwindow()
    window.show()
    # ser = scom.spopen()
    # status = app.exec_()
    sys.exit(app.exec_())
    # print(status)

    # sys.exit(status)