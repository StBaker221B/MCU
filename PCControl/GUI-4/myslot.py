
from scom import spcom
from PyQt5 import QtCore, QtGui, QtWidgets

def btn_C_0_clicked(ser, state):
    # print(state)
    if(state):
        spcom(ser, b'C00\r\n')
    else:
        spcom(ser, b'C01\r\n')

def btn_C_1_clicked(ser, state):
    # spcom(b'C1\r\n')
    if(state):
        spcom(ser, b'C10\r\n')
    else:
        spcom(ser, b'C11\r\n')


def btn_C_2_clicked():
    spcom(b'C2\r\n')

def btn_C_3_clicked():
    spcom(b'C3\r\n')

def btn_C_4_clicked():
    spcom(b'C4\r\n')

def btn_C_5_clicked():
    spcom(b'C5\r\n')

def btn_C_6_clicked():
    spcom(b'C6\r\n')

def btn_C_7_clicked():
    spcom(b'C7\r\n')

def btn_C_8_clicked():
    spcom(b'C8\r\n')

def btn_C_9_clicked():
    spcom(b'C9\r\n')


