
from spcom import spcom
from PyQt5 import QtCore, QtGui, QtWidgets

# PSA 1
def BTN_PSA1_IN_clicked(ser, state):
    if(state):
        spcom(ser, b'PSA1 IN   1\r\n')
    else:
        spcom(ser, b'PSA1 IN   0\r\n')

def BTN_PSA1_PRO_clicked(ser, state):
    if(state):
        spcom(ser, b'PSA1 PRO  1\r\n')
    else:
        spcom(ser, b'PSA1 PRO  0\r\n')

def BTN_PSA1_BAL_clicked(ser, state):
    if(state):
        spcom(ser, b'PSA1 BAL  1\r\n')
    else:
        spcom(ser, b'PSA1 BAL  0\r\n')

def BTN_PSA1_CLR_clicked(ser, state):
    if(state):
        spcom(ser, b'PSA1 CLR  1\r\n')
    else:
        spcom(ser, b'PSA1 CLR  0\r\n')

# PSA 2
def BTN_PSA2_IN_clicked(ser, state):
    if(state):
        spcom(ser, b'PSA2 IN   1\r\n')
    else:
        spcom(ser, b'PSA2 IN   0\r\n')

def BTN_PSA2_PRO_clicked(ser, state):
    if(state):
        spcom(ser, b'PSA2 PRO  1\r\n')
    else:
        spcom(ser, b'PSA2 PRO  0\r\n')

def BTN_PSA2_BAL_clicked(ser, state):
    if(state):
        spcom(ser, b'PSA2 BAL  1\r\n')
    else:
        spcom(ser, b'PSA2 BAL  0\r\n')

def BTN_PSA2_CLR_clicked(ser, state):
    if(state):
        spcom(ser, b'PSA2 CLR  1\r\n')
    else:
        spcom(ser, b'PSA2 CLR  0\r\n')

# PROD 
def BTN_PROD_OUT_clicked(ser, state):
    # print("prod_out")
    if(state):
        spcom(ser, b'PROD OUT  1\r\n')
    else:
        spcom(ser, b'PROD OUT  0\r\n')

def BTN_PROD_PSA1_clicked(ser, state):
    if(state):
        spcom(ser, b'PROD PSA1 1\r\n')
    else:
        spcom(ser, b'PROD PSA1 0\r\n')

def BTN_PROD_PSA2_clicked(ser, state):
    if(state):
        spcom(ser, b'PROD PSA2 1\r\n')
    else:
        spcom(ser, b'PROD PSA2 0\r\n')

# COL2 
def BTN_COL2_IN_clicked(ser, state):
    if(state):
        spcom(ser, b'COL2 IN   1\r\n')
    else:
        spcom(ser, b'COL2 IN   0\r\n')

# def btn_C_9_clicked():
#     spcom(b'C9\r\n')

def setAutostart(ser):
    spcom(ser, b'SET START\r\n')
    # print("SET START")

def setAutorepeat(ser):
    spcom(ser, b'SET REPEAT\r\n')

def setManual(ser):
    spcom(ser, b'SET MANUAL\r\n')

def setRun(ser):
    spcom(ser, b'RUN\r\n')

def setPause(ser):
    spcom(ser, b'PAUSE\r\n')

def timeUpdate(time, ui):
    ui.lcdTIME.display(time)
    cs = ui.labelControlState.text()
    if(cs == "AUTO_START"):
        if(time == 1.0):
            ui.label_statePSA1.setText("charge")
            ui.label_statePSA2.setText("off")
        elif(time == 2.0):
            ui.label_statePSA1.setText("work")
            ui.label_statePSA2.setText("off")
        elif(time == 4.0):
            ui.label_statePSA1.setText("balance")
            ui.label_statePSA2.setText("charge")
        elif(time == 5.0):
            ui.label_statePSA1.setText("sweep")
            ui.label_statePSA2.setText("work")
        elif(time == 6.0):
            ui.label_statePSA1.setText("off")
            ui.label_statePSA2.setText("work")
        elif(time == 7.0):
            ui.label_statePSA1.setText("charge")
            ui.label_statePSA2.setText("balance")
        elif(time == 8.0):
            ui.label_statePSA1.setText("work")
            ui.label_statePSA2.setText("sweep")
        # elif(time == 9.0):
        #     ui.label_statePSA1.setText("work")
        #     ui.label_statePSA2.setText("off")
    elif(cs == "AUTO_REPEAT"):
        if(time == 1.0):
            ui.label_statePSA1.setText("work")
            ui.label_statePSA2.setText("off")
        elif(time == 2.0):
            ui.label_statePSA1.setText("balance")
            ui.label_statePSA2.setText("charge")
        elif(time == 3.0):
            ui.label_statePSA1.setText("sweep")
            ui.label_statePSA2.setText("work")
        elif(time == 4.0):
            ui.label_statePSA1.setText("off")
            ui.label_statePSA2.setText("work")
        elif(time == 5.0):
            ui.label_statePSA1.setText("charge")
            ui.label_statePSA2.setText("balance")
        elif(time == 6.0):
            ui.label_statePSA1.setText("work")
            ui.label_statePSA2.setText("sweep")
    elif(cs == "MANUAL"):
        ui.label_statePSA1.setText("MANUAL")
        ui.label_statePSA2.setText("MANUAL")

def controlUpdate(cs, ui):
    ui.labelControlState.setText(cs)

def valveUpdate(report, ui):
    section = report[1]
    function = report[2]

    if(section == 'PSA1'):
        if(function == 'IN'):
            # switch = window.switchTable[section][0]
            switch = ui.BTN_PSA1_IN
            id = 0
        elif(function == 'PRO'):
            # switch = window.switchTable[section][1]
            switch = ui.BTN_PSA1_PRO
            id = 1
        elif(function == 'BAL'):
            # switch = window.switchTable[section][2]
            switch = ui.BTN_PSA1_BAL
            id = 2
        elif(function == 'CLR'):
            # switch = window.switchTable[section][3]
            switch = ui.BTN_PSA1_CLR
            id = 3
    elif(section == 'PSA2'):
        if(function == 'IN'):
            # switch = window.switchTable[section][0]
            switch = ui.BTN_PSA2_IN
            id = 4
        elif(function == 'PRO'):
            # switch = window.switchTable[section][1]
            switch = ui.BTN_PSA2_PRO
            id = 5
        elif(function == 'BAL'):
            # switch = window.switchTable[section][2]
            switch = ui.BTN_PSA2_BAL
            id = 6
        elif(function == 'CLR'):
            # switch = window.switchTable[section][3]
            switch = ui.BTN_PSA2_CLR
            id = 7
    elif(section == 'PROD'):
        if(function == 'OUT'):
            # switch = window.switchTable[section][0]
            switch = ui.BTN_PROD_OUT
            id = 8
        elif(function == 'PSA1'):
            # switch = window.switchTable[section][1]
            switch = ui.BTN_PROD_PSA1
            id = 9
        elif(function == 'PSA2'):
            # switch = window.switchTable[section][2]
            switch = ui.BTN_PROD_PSA2
            id = 10
    elif(section == 'COL2'):
        if(function == 'IN'):
            # switch = window.switchTable[section][0]
            switch = ui.BTN_COL2_IN
            id = 11
            
    # print(switch.isChecked())
    if(report[3] == '1'):
        item = QtWidgets.QTableWidgetItem("ON")        
        ui.table_ValveList.setItem(id, 0, item)
        switch.setIcon(ui.icon_btnOn)
        if(not switch.isChecked()):
            switch.toggle()
    elif(report[3] == '0'):
        item = QtWidgets.QTableWidgetItem("OFF")        
        ui.table_ValveList.setItem(id, 0, item)
        switch.setIcon(ui.icon_btnOff)
        if(switch.isChecked()):
            switch.toggle()

def BTN_OK_clicked(dlg):
    dlg.close()