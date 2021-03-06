# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BTN_PSA1_IN = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_PSA1_IN.setGeometry(QtCore.QRect(120, 70, 40, 40))
        self.BTN_PSA1_IN.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./resource/valveoff.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/logo_valve/resource/valveon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.BTN_PSA1_IN.setIcon(icon)
        self.BTN_PSA1_IN.setIconSize(QtCore.QSize(32, 32))
        self.BTN_PSA1_IN.setCheckable(True)
        self.BTN_PSA1_IN.setObjectName("BTN_PSA1_IN")
        self.BTN_PSA1_PRO = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_PSA1_PRO.setGeometry(QtCore.QRect(120, 140, 40, 40))
        self.BTN_PSA1_PRO.setIcon(icon)
        self.BTN_PSA1_PRO.setIconSize(QtCore.QSize(32, 32))
        self.BTN_PSA1_PRO.setCheckable(True)
        self.BTN_PSA1_PRO.setObjectName("BTN_PSA1_PRO")
        self.BTN_PSA1_BAL = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_PSA1_BAL.setGeometry(QtCore.QRect(530, 120, 40, 40))
        self.BTN_PSA1_BAL.setIcon(icon)
        self.BTN_PSA1_BAL.setIconSize(QtCore.QSize(32, 32))
        self.BTN_PSA1_BAL.setCheckable(True)
        self.BTN_PSA1_BAL.setObjectName("BTN_PSA1_BAL")
        self.BTN_PSA1_CLR = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_PSA1_CLR.setGeometry(QtCore.QRect(530, 40, 40, 40))
        self.BTN_PSA1_CLR.setIcon(icon)
        self.BTN_PSA1_CLR.setIconSize(QtCore.QSize(32, 32))
        self.BTN_PSA1_CLR.setCheckable(True)
        self.BTN_PSA1_CLR.setObjectName("BTN_PSA1_CLR")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 80, 521, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line.setFont(font)
        self.line.setAutoFillBackground(False)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setMidLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(80, 340, 471, 20))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(70, 90, 20, 261))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(540, 90, 20, 261))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setObjectName("line_4")
        self.BTN_PSA2_IN = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_PSA2_IN.setGeometry(QtCore.QRect(120, 330, 40, 40))
        self.BTN_PSA2_IN.setText("")
        self.BTN_PSA2_IN.setIcon(icon)
        self.BTN_PSA2_IN.setIconSize(QtCore.QSize(32, 32))
        self.BTN_PSA2_IN.setCheckable(True)
        self.BTN_PSA2_IN.setObjectName("BTN_PSA2_IN")
        self.BTN_PSA2_BAL = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_PSA2_BAL.setGeometry(QtCore.QRect(530, 280, 40, 40))
        self.BTN_PSA2_BAL.setIcon(icon)
        self.BTN_PSA2_BAL.setIconSize(QtCore.QSize(32, 32))
        self.BTN_PSA2_BAL.setCheckable(True)
        self.BTN_PSA2_BAL.setObjectName("BTN_PSA2_BAL")
        self.BTN_PSA2_CLR = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_PSA2_CLR.setGeometry(QtCore.QRect(530, 360, 40, 40))
        self.BTN_PSA2_CLR.setIcon(icon)
        self.BTN_PSA2_CLR.setIconSize(QtCore.QSize(32, 32))
        self.BTN_PSA2_CLR.setCheckable(True)
        self.BTN_PSA2_CLR.setObjectName("BTN_PSA2_CLR")
        self.BTN_PSA2_PRO = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_PSA2_PRO.setGeometry(QtCore.QRect(120, 260, 40, 40))
        self.BTN_PSA2_PRO.setIcon(icon)
        self.BTN_PSA2_PRO.setIconSize(QtCore.QSize(32, 32))
        self.BTN_PSA2_PRO.setCheckable(True)
        self.BTN_PSA2_PRO.setObjectName("BTN_PSA2_PRO")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(480, 90, 20, 41))
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setLineWidth(3)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(140, 120, 351, 20))
        self.line_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_6.setLineWidth(3)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setObjectName("line_6")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(200, 60, 251, 51))
        self.graphicsView.setObjectName("graphicsView")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(140, 300, 351, 20))
        self.line_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_7.setLineWidth(3)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(480, 310, 20, 41))
        self.line_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_8.setLineWidth(3)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setObjectName("line_8")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(200, 330, 251, 51))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(130, 130, 20, 181))
        self.line_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_9.setLineWidth(3)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(140, 210, 321, 20))
        self.line_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_10.setLineWidth(3)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setObjectName("line_10")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_3.setGeometry(QtCore.QRect(200, 200, 211, 51))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.BTN_PROD_OUT = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_PROD_OUT.setGeometry(QtCore.QRect(490, 220, 40, 40))
        self.BTN_PROD_OUT.setIcon(icon)
        self.BTN_PROD_OUT.setIconSize(QtCore.QSize(32, 32))
        self.BTN_PROD_OUT.setCheckable(True)
        self.BTN_PROD_OUT.setObjectName("BTN_PROD_OUT")
        self.BTN_PROD_PSA1 = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_PROD_PSA1.setGeometry(QtCore.QRect(440, 150, 40, 40))
        self.BTN_PROD_PSA1.setIcon(icon)
        self.BTN_PROD_PSA1.setIconSize(QtCore.QSize(32, 32))
        self.BTN_PROD_PSA1.setCheckable(True)
        self.BTN_PROD_PSA1.setObjectName("BTN_PROD_PSA1")
        self.BTN_PROD_PSA2 = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_PROD_PSA2.setGeometry(QtCore.QRect(440, 260, 40, 40))
        self.BTN_PROD_PSA2.setIcon(icon)
        self.BTN_PROD_PSA2.setIconSize(QtCore.QSize(32, 32))
        self.BTN_PROD_PSA2.setCheckable(True)
        self.BTN_PROD_PSA2.setObjectName("BTN_PROD_PSA2")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(450, 170, 20, 91))
        self.line_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_11.setLineWidth(3)
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setGeometry(QtCore.QRect(210, 160, 251, 20))
        self.line_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_12.setLineWidth(3)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setObjectName("line_12")
        self.line_13 = QtWidgets.QFrame(self.centralwidget)
        self.line_13.setGeometry(QtCore.QRect(210, 270, 251, 20))
        self.line_13.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_13.setLineWidth(3)
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setObjectName("line_13")
        self.line_14 = QtWidgets.QFrame(self.centralwidget)
        self.line_14.setGeometry(QtCore.QRect(200, 110, 20, 61))
        self.line_14.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_14.setLineWidth(3)
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setObjectName("line_14")
        self.line_15 = QtWidgets.QFrame(self.centralwidget)
        self.line_15.setGeometry(QtCore.QRect(200, 280, 20, 51))
        self.line_15.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_15.setLineWidth(3)
        self.line_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_15.setObjectName("line_15")
        self.line_16 = QtWidgets.QFrame(self.centralwidget)
        self.line_16.setGeometry(QtCore.QRect(450, 360, 81, 20))
        self.line_16.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_16.setLineWidth(3)
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setObjectName("line_16")
        self.line_17 = QtWidgets.QFrame(self.centralwidget)
        self.line_17.setGeometry(QtCore.QRect(450, 60, 81, 20))
        self.line_17.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_17.setLineWidth(3)
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setObjectName("line_17")
        self.line_18 = QtWidgets.QFrame(self.centralwidget)
        self.line_18.setGeometry(QtCore.QRect(410, 230, 81, 20))
        self.line_18.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_18.setLineWidth(3)
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setObjectName("line_18")
        self.line_19 = QtWidgets.QFrame(self.centralwidget)
        self.line_19.setGeometry(QtCore.QRect(530, 230, 81, 20))
        self.line_19.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_19.setLineWidth(3)
        self.line_19.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_19.setObjectName("line_19")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 60, 101, 51))
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 330, 101, 51))
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 200, 101, 51))
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setObjectName("label_3")
        self.BTN_COL2_IN = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_COL2_IN.setGeometry(QtCore.QRect(50, 20, 40, 40))
        self.BTN_COL2_IN.setIcon(icon)
        self.BTN_COL2_IN.setIconSize(QtCore.QSize(32, 32))
        self.BTN_COL2_IN.setCheckable(True)
        self.BTN_COL2_IN.setObjectName("BTN_COL2_IN")
        self.line_13.raise_()
        self.line_12.raise_()
        self.line_11.raise_()
        self.line_9.raise_()
        self.line_6.raise_()
        self.line_4.raise_()
        self.line.raise_()
        self.BTN_PSA1_PRO.raise_()
        self.BTN_PSA1_CLR.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.BTN_PSA1_BAL.raise_()
        self.BTN_PSA1_IN.raise_()
        self.BTN_PSA2_IN.raise_()
        self.BTN_PSA2_BAL.raise_()
        self.BTN_PSA2_CLR.raise_()
        self.BTN_PSA2_PRO.raise_()
        self.line_5.raise_()
        self.graphicsView.raise_()
        self.line_7.raise_()
        self.line_8.raise_()
        self.graphicsView_2.raise_()
        self.line_10.raise_()
        self.graphicsView_3.raise_()
        self.BTN_PROD_OUT.raise_()
        self.BTN_PROD_PSA1.raise_()
        self.BTN_PROD_PSA2.raise_()
        self.line_14.raise_()
        self.line_15.raise_()
        self.line_16.raise_()
        self.line_17.raise_()
        self.line_18.raise_()
        self.line_19.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.BTN_COL2_IN.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        self.menuControl = QtWidgets.QMenu(self.menubar)
        self.menuControl.setObjectName("menuControl")
        self.menuAuto = QtWidgets.QMenu(self.menuControl)
        self.menuAuto.setObjectName("menuAuto")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionManual = QtWidgets.QAction(MainWindow)
        self.actionManual.setObjectName("actionManual")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionStart = QtWidgets.QAction(MainWindow)
        self.actionStart.setObjectName("actionStart")
        self.actionRepeat = QtWidgets.QAction(MainWindow)
        self.actionRepeat.setObjectName("actionRepeat")
        self.menuAuto.addAction(self.actionStart)
        self.menuAuto.addAction(self.actionRepeat)
        self.menuControl.addAction(self.menuAuto.menuAction())
        self.menuControl.addAction(self.actionManual)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuControl.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setToolTip(_translate("MainWindow", "PSA1_PRO"))
        self.BTN_PSA1_IN.setToolTip(_translate("MainWindow", "PSA1_IN"))
        self.BTN_PSA1_PRO.setToolTip(_translate("MainWindow", "PSA1_PRO"))
        self.BTN_PSA1_BAL.setToolTip(_translate("MainWindow", "PSA1_BAL"))
        self.BTN_PSA1_CLR.setToolTip(_translate("MainWindow", "PSA1_CLR"))
        self.BTN_PSA2_IN.setToolTip(_translate("MainWindow", "PSA2_IN"))
        self.BTN_PSA2_BAL.setToolTip(_translate("MainWindow", "PSA2_BAL"))
        self.BTN_PSA2_CLR.setToolTip(_translate("MainWindow", "PSA2_CLR"))
        self.BTN_PSA2_PRO.setToolTip(_translate("MainWindow", "PSA2_PRO"))
        self.BTN_PROD_OUT.setToolTip(_translate("MainWindow", "PROD_OUT"))
        self.BTN_PROD_PSA1.setToolTip(_translate("MainWindow", "PROD_PSA1"))
        self.BTN_PROD_PSA2.setToolTip(_translate("MainWindow", "PROD_PSA2"))
        self.label.setText(_translate("MainWindow", "PSA 1"))
        self.label_2.setText(_translate("MainWindow", "PSA 2"))
        self.label_3.setText(_translate("MainWindow", "PROD"))
        self.BTN_COL2_IN.setToolTip(_translate("MainWindow", "COL2_IN"))
        self.menuControl.setTitle(_translate("MainWindow", "Control"))
        self.menuAuto.setTitle(_translate("MainWindow", "Auto"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionManual.setText(_translate("MainWindow", "Manual"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionStart.setText(_translate("MainWindow", "Start"))
        self.actionRepeat.setText(_translate("MainWindow", "Repeat"))
import res_rc
