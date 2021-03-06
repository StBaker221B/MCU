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
        MainWindow.resize(480, 270)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 160, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.button_C_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_C_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo_switch/resource/switchoff_128px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/logo_switch/resource/switchon_128px.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.button_C_3.setIcon(icon)
        self.button_C_3.setIconSize(QtCore.QSize(32, 19))
        self.button_C_3.setCheckable(True)
        self.button_C_3.setObjectName("button_C_3")
        self.gridLayout.addWidget(self.button_C_3, 3, 1, 1, 1)
        self.label_C_0 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_C_0.setFont(font)
        self.label_C_0.setObjectName("label_C_0")
        self.gridLayout.addWidget(self.label_C_0, 0, 0, 1, 1)
        self.button_C_0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_C_0.setAutoFillBackground(False)
        self.button_C_0.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./resource/switchoff_128px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("./resource/switchon_128px.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.button_C_0.setIcon(icon1)
        self.button_C_0.setIconSize(QtCore.QSize(32, 19))
        self.button_C_0.setCheckable(True)
        self.button_C_0.setChecked(False)
        self.button_C_0.setObjectName("button_C_0")
        self.gridLayout.addWidget(self.button_C_0, 0, 1, 1, 1)
        self.button_C_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_C_1.setText("")
        self.button_C_1.setIcon(icon)
        self.button_C_1.setIconSize(QtCore.QSize(32, 19))
        self.button_C_1.setCheckable(True)
        self.button_C_1.setObjectName("button_C_1")
        self.gridLayout.addWidget(self.button_C_1, 1, 1, 1, 1)
        self.label_C_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_C_1.setFont(font)
        self.label_C_1.setObjectName("label_C_1")
        self.gridLayout.addWidget(self.label_C_1, 1, 0, 1, 1)
        self.button_C_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_C_2.setText("")
        self.button_C_2.setIcon(icon)
        self.button_C_2.setIconSize(QtCore.QSize(32, 19))
        self.button_C_2.setCheckable(True)
        self.button_C_2.setObjectName("button_C_2")
        self.gridLayout.addWidget(self.button_C_2, 2, 1, 1, 1)
        self.label_C_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_C_3.setFont(font)
        self.label_C_3.setObjectName("label_C_3")
        self.gridLayout.addWidget(self.label_C_3, 3, 0, 1, 1)
        self.label_C_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_C_2.setFont(font)
        self.label_C_2.setObjectName("label_C_2")
        self.gridLayout.addWidget(self.label_C_2, 2, 0, 1, 1)
        self.label_C_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_C_4.setFont(font)
        self.label_C_4.setObjectName("label_C_4")
        self.gridLayout.addWidget(self.label_C_4, 4, 0, 1, 1)
        self.button_C_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_C_4.setText("")
        self.button_C_4.setIcon(icon)
        self.button_C_4.setIconSize(QtCore.QSize(32, 19))
        self.button_C_4.setCheckable(True)
        self.button_C_4.setObjectName("button_C_4")
        self.gridLayout.addWidget(self.button_C_4, 4, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(210, 20, 160, 191))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.button_C_5 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.button_C_5.setText("")
        self.button_C_5.setIcon(icon)
        self.button_C_5.setIconSize(QtCore.QSize(32, 19))
        self.button_C_5.setCheckable(True)
        self.button_C_5.setObjectName("button_C_5")
        self.gridLayout_2.addWidget(self.button_C_5, 3, 1, 1, 1)
        self.label_C_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_C_5.setFont(font)
        self.label_C_5.setObjectName("label_C_5")
        self.gridLayout_2.addWidget(self.label_C_5, 0, 0, 1, 1)
        self.button_C_6 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.button_C_6.setAutoFillBackground(True)
        self.button_C_6.setText("")
        self.button_C_6.setIcon(icon)
        self.button_C_6.setIconSize(QtCore.QSize(32, 19))
        self.button_C_6.setCheckable(True)
        self.button_C_6.setChecked(False)
        self.button_C_6.setObjectName("button_C_6")
        self.gridLayout_2.addWidget(self.button_C_6, 0, 1, 1, 1)
        self.button_C_7 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.button_C_7.setText("")
        self.button_C_7.setIcon(icon)
        self.button_C_7.setIconSize(QtCore.QSize(32, 19))
        self.button_C_7.setCheckable(True)
        self.button_C_7.setObjectName("button_C_7")
        self.gridLayout_2.addWidget(self.button_C_7, 1, 1, 1, 1)
        self.label_C_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_C_6.setFont(font)
        self.label_C_6.setObjectName("label_C_6")
        self.gridLayout_2.addWidget(self.label_C_6, 1, 0, 1, 1)
        self.button_C_8 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.button_C_8.setText("")
        self.button_C_8.setIcon(icon)
        self.button_C_8.setIconSize(QtCore.QSize(32, 19))
        self.button_C_8.setCheckable(True)
        self.button_C_8.setObjectName("button_C_8")
        self.gridLayout_2.addWidget(self.button_C_8, 2, 1, 1, 1)
        self.label_C_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_C_7.setFont(font)
        self.label_C_7.setObjectName("label_C_7")
        self.gridLayout_2.addWidget(self.label_C_7, 3, 0, 1, 1)
        self.label_C_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_C_8.setFont(font)
        self.label_C_8.setObjectName("label_C_8")
        self.gridLayout_2.addWidget(self.label_C_8, 2, 0, 1, 1)
        self.label_C_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_C_9.setFont(font)
        self.label_C_9.setObjectName("label_C_9")
        self.gridLayout_2.addWidget(self.label_C_9, 4, 0, 1, 1)
        self.button_C_9 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.button_C_9.setText("")
        self.button_C_9.setIcon(icon)
        self.button_C_9.setIconSize(QtCore.QSize(32, 19))
        self.button_C_9.setCheckable(True)
        self.button_C_9.setObjectName("button_C_9")
        self.gridLayout_2.addWidget(self.button_C_9, 4, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 18))
        self.menubar.setObjectName("menubar")
        self.menuControl = QtWidgets.QMenu(self.menubar)
        self.menuControl.setObjectName("menuControl")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAuto = QtWidgets.QAction(MainWindow)
        self.actionAuto.setObjectName("actionAuto")
        self.actionManual = QtWidgets.QAction(MainWindow)
        self.actionManual.setObjectName("actionManual")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuControl.addAction(self.actionAuto)
        self.menuControl.addAction(self.actionManual)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuControl.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_C_0.setText(_translate("MainWindow", "LED 0"))
        self.label_C_1.setText(_translate("MainWindow", "LED 1"))
        self.label_C_3.setText(_translate("MainWindow", "S 3"))
        self.label_C_2.setText(_translate("MainWindow", "S 2"))
        self.label_C_4.setText(_translate("MainWindow", "S 4"))
        self.label_C_5.setText(_translate("MainWindow", "S 5"))
        self.label_C_6.setText(_translate("MainWindow", "S 6"))
        self.label_C_7.setText(_translate("MainWindow", "S 8"))
        self.label_C_8.setText(_translate("MainWindow", "S 7"))
        self.label_C_9.setText(_translate("MainWindow", "S 9"))
        self.menuControl.setTitle(_translate("MainWindow", "Control"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAuto.setText(_translate("MainWindow", "Auto"))
        self.actionManual.setText(_translate("MainWindow", "Manual"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
import res_rc
