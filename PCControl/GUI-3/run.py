
from PyQt5 import QtWidgets
from mainwindow import Ui_MainWindow
import sys

import mwdef

class mainwindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mainwindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.button_C_0.clicked.connect(mwdef.btn_C_0_clicked)
        self.ui.button_C_1.clicked.connect(mwdef.btn_C_1_clicked)
        self.ui.button_C_2.clicked.connect(mwdef.btn_C_2_clicked)
        self.ui.button_C_3.clicked.connect(mwdef.btn_C_3_clicked)
        self.ui.button_C_4.clicked.connect(mwdef.btn_C_4_clicked)
        self.ui.button_C_5.clicked.connect(mwdef.btn_C_5_clicked)
        self.ui.button_C_6.clicked.connect(mwdef.btn_C_6_clicked)
        self.ui.button_C_7.clicked.connect(mwdef.btn_C_7_clicked)
        self.ui.button_C_8.clicked.connect(mwdef.btn_C_8_clicked)
        self.ui.button_C_9.clicked.connect(mwdef.btn_C_9_clicked)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = mainwindow()
    window.show()
    sys.exit(app.exec())