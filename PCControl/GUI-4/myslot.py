
from scom import spcom
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
    spcom(ser, b'SET START')

def setAutorepeat(ser):
    spcom(ser, b'SET REPEAT ')

def setManual(ser):
    spcom(ser, b'SET MANUAL ')


