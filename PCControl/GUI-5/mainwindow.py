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
        MainWindow.resize(810, 499)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Background = QtWidgets.QGraphicsView(self.centralwidget)
        self.Background.setGeometry(QtCore.QRect(-5, -19, 911, 501))
        self.Background.setAutoFillBackground(False)
        self.Background.setStyleSheet("")
        self.Background.setLineWidth(2)
        self.Background.setObjectName("Background")
        self.frameBTNPanel = QtWidgets.QFrame(self.centralwidget)
        self.frameBTNPanel.setGeometry(QtCore.QRect(10, 10, 571, 441))
        self.frameBTNPanel.setFrameShape(QtWidgets.QFrame.Box)
        self.frameBTNPanel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameBTNPanel.setLineWidth(2)
        self.frameBTNPanel.setObjectName("frameBTNPanel")
        self.groupBox_valve = QtWidgets.QGroupBox(self.frameBTNPanel)
        self.groupBox_valve.setGeometry(QtCore.QRect(10, 10, 551, 421))
        self.groupBox_valve.setMouseTracking(True)
        self.groupBox_valve.setAutoFillBackground(False)
        self.groupBox_valve.setFlat(True)
        self.groupBox_valve.setCheckable(False)
        self.groupBox_valve.setObjectName("groupBox_valve")
        self.BTN_COL2_IN = QtWidgets.QPushButton(self.groupBox_valve)
        self.BTN_COL2_IN.setGeometry(QtCore.QRect(30, 30, 40, 40))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./resource/valveoff.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/logo_valve/resource/valveon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.BTN_COL2_IN.setIcon(icon)
        self.BTN_COL2_IN.setIconSize(QtCore.QSize(32, 32))
        self.BTN_COL2_IN.setCheckable(True)
        self.BTN_COL2_IN.setObjectName("BTN_COL2_IN")
        self.label_3 = QtWidgets.QLabel(self.groupBox_valve)
        self.label_3.setGeometry(QtCore.QRect(160, 200, 211, 51))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setText("")
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setPixmap(QtGui.QPixmap(":/logo_vessel/resource/prodvessel.png"))
        self.label_3.setObjectName("label_3")
        self.BTN_PSA2_PRO = QtWidgets.QPushButton(self.groupBox_valve)
        self.BTN_PSA2_PRO.setGeometry(QtCore.QRect(80, 260, 40, 40))
        self.BTN_PSA2_PRO.setIcon(icon)
        self.BTN_PSA2_PRO.setIconSize(QtCore.QSize(32, 32))
        self.BTN_PSA2_PRO.setCheckable(True)
        self.BTN_PSA2_PRO.setObjectName("BTN_PSA2_PRO")
        self.line_11 = QtWidgets.QFrame(self.groupBox_valve)
        self.line_11.setGeometry(QtCore.QRect(410, 170, 20, 91))
        self.line_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_11.setLineWidth(3)
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setObjectName("line_11")
        self.line_16 = QtWidgets.QFrame(self.groupBox_valve)
        self.line_16.setGeometry(QtCore.QRect(410, 360, 81, 20))
        self.line_16.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_16.setLineWidth(3)
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setObjectName("line_16")
        self.line_13 = QtWidgets.QFrame(self.groupBox_valve)
        self.line_13.setGeometry(QtCore.QRect(170, 270, 251, 20))
        self.line_13.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_13.setLineWidth(3)
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setObjectName("line_13")
        self.PROD = QtWidgets.QGraphicsView(self.groupBox_valve)
        self.PROD.setGeometry(QtCore.QRect(160, 200, 211, 51))
        self.PROD.setAutoFillBackground(True)
        self.PROD.setObjectName("PROD")
        self.line_7 = QtWidgets.QFrame(self.groupBox_valve)
        self.line_7.setGeometry(QtCore.QRect(100, 300, 351, 20))
        self.line_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_7.setLineWidth(3)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setObjectName("line_7")
        self.graphicsView = QtWidgets.QGraphicsView(self.groupBox_valve)
        self.graphicsView.setGeometry(QtCore.QRect(160, 60, 251, 51))
        self.graphicsView.setAutoFillBackground(True)
        self.graphicsView.setObjectName("graphicsView")
        self.line_6 = QtWidgets.QFrame(self.groupBox_valve)
        self.line_6.setGeometry(QtCore.QRect(100, 120, 351, 20))
        self.line_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_6.setLineWidth(3)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setObjectName("line_6")
        self.line_15 = QtWidgets.QFrame(self.groupBox_valve)
        self.line_15.setGeometry(QtCore.QRect(160, 280, 20, 51))
        self.line_15.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_15.setLineWidth(3)
        self.line_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_15.setObjectName("line_15")
        self.line_4 = QtWidgets.QFrame(self.groupBox_valve)
        self.line_4.setGeometry(QtCore.QRect(500, 90, 20, 261))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setObjectName("line_4")
        self.BTN_PSA2_IN = QtWidgets.QPushButton(self.groupBox_valve)
        self.BTN_PSA2_IN.setGeometry(QtCore.QRect(80, 330, 40, 40))
        self.BTN_PSA2_IN.setText("")
        self.BTN_PSA2_IN.setIcon(icon)
        self.BTN_PSA2_IN.setIconSize(QtCore.QSize(32, 32))
        self.BTN_PSA2_IN.setCheckable(True)
        self.BTN_PSA2_IN.setObjectName("BTN_PSA2_IN")
        self.line_12 = QtWidgets.QFrame(self.groupBox_valve)
        self.line_12.setGeometry(QtCore.QRect(170, 160, 251, 20))
        self.line_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_12.setLineWidth(3)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setObjectName("line_12")
        self.label_2 = QtWidgets.QLabel(self.groupBox_valve)
        self.label_2.setGeometry(QtCore.QRect(160, 330, 251, 51))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setText("")
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setPixmap(QtGui.QPixmap(":/logo_vessel/resource/psavessel.png"))
        self.label_2.setObjectName("label_2")
        self.BTN_PSA2_BAL = QtWidgets.QPushButton(self.groupBox_valve)
        self.BTN_PSA2_BAL.setGeometry(QtCore.QRect(490, 280, 40, 40))
        self.BTN_PSA2_BAL.setIcon(icon)
        self.BTN_PSA2_BAL.setIconSize(QtCore.QSize(32, 32))
        self.BTN_PSA2_BAL.setCheckable(True)
        self.BTN_PSA2_BAL.setObjectName("BTN_PSA2_BAL")
        self.BTN_PSA1_BAL = QtWidgets.QPushButton(self.groupBox_valve)
        self.BTN_PSA1_BAL.setGeometry(QtCore.QRect(490, 120, 40, 40))
        self.BTN_PSA1_BAL.setIcon(icon)
        self.BTN_PSA1_BAL.setIconSize(QtCore.QSize(32, 32))
        self.BTN_PSA1_BAL.setCheckable(True)
        self.BTN_PSA1_BAL.setObjectName("BTN_PSA1_BAL")
        self.line_9 = QtWidgets.QFrame(self.groupBox_valve)
        self.line_9.setGeometry(QtCore.QRect(90, 130, 20, 181))
        self.line_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_9.setLineWidth(3)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setObjectName("line_9")
        self.BTN_PSA2_CLR = QtWidgets.QPushButton(self.groupBox_valve)
        self.BTN_PSA2_CLR.setGeometry(QtCore.QRect(490, 360, 40, 40))
        self.BTN_PSA2_CLR.setIcon(icon)
        self.BTN_PSA2_CLR.setIconSize(QtCore.QSize(32, 32))
        self.BTN_PSA2_CLR.setCheckable(True)
        self.BTN_PSA2_CLR.setObjectName("BTN_PSA2_CLR")
        self.BTN_PROD_OUT = QtWidgets.QPushButton(self.groupBox_valve)
        self.BTN_PROD_OUT.setGeometry(QtCore.QRect(450, 220, 40, 40))
        self.BTN_PROD_OUT.setIcon(icon)
        self.BTN_PROD_OUT.setIconSize(QtCore.QSize(32, 32))
        self.BTN_PROD_OUT.setCheckable(True)
        self.BTN_PROD_OUT.setObjectName("BTN_PROD_OUT")
        self.BTN_PROD_PSA2 = QtWidgets.QPushButton(self.groupBox_valve)
        self.BTN_PROD_PSA2.setGeometry(QtCore.QRect(400, 260, 40, 40))
        self.BTN_PROD_PSA2.setIcon(icon)
        self.BTN_PROD_PSA2.setIconSize(QtCore.QSize(32, 32))
        self.BTN_PROD_PSA2.setCheckable(True)
        self.BTN_PROD_PSA2.setObjectName("BTN_PROD_PSA2")
        self.line_10 = QtWidgets.QFrame(self.groupBox_valve)
        self.line_10.setGeometry(QtCore.QRect(100, 210, 321, 20))
        self.line_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_10.setLineWidth(3)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setObjectName("line_10")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.groupBox_valve)
        self.graphicsView_2.setGeometry(QtCore.QRect(160, 330, 251, 51))
        self.graphicsView_2.setAutoFillBackground(True)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.BTN_PSA1_IN = QtWidgets.QPushButton(self.groupBox_valve)
        self.BTN_PSA1_IN.setGeometry(QtCore.QRect(80, 70, 40, 40))
        self.BTN_PSA1_IN.setText("")
        self.BTN_PSA1_IN.setIcon(icon)
        self.BTN_PSA1_IN.setIconSize(QtCore.QSize(32, 32))
        self.BTN_PSA1_IN.setCheckable(True)
        self.BTN_PSA1_IN.setObjectName("BTN_PSA1_IN")
        self.line_3 = QtWidgets.QFrame(self.groupBox_valve)
        self.line_3.setGeometry(QtCore.QRect(30, 90, 20, 261))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.line_8 = QtWidgets.QFrame(self.groupBox_valve)
        self.line_8.setGeometry(QtCore.QRect(440, 310, 20, 41))
        self.line_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_8.setLineWidth(3)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setObjectName("line_8")
        self.line_5 = QtWidgets.QFrame(self.groupBox_valve)
        self.line_5.setGeometry(QtCore.QRect(440, 90, 20, 41))
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setLineWidth(3)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setObjectName("line_5")
        self.BTN_PSA1_CLR = QtWidgets.QPushButton(self.groupBox_valve)
        self.BTN_PSA1_CLR.setGeometry(QtCore.QRect(490, 40, 40, 40))
        self.BTN_PSA1_CLR.setIcon(icon)
        self.BTN_PSA1_CLR.setIconSize(QtCore.QSize(32, 32))
        self.BTN_PSA1_CLR.setCheckable(True)
        self.BTN_PSA1_CLR.setObjectName("BTN_PSA1_CLR")
        self.line_17 = QtWidgets.QFrame(self.groupBox_valve)
        self.line_17.setGeometry(QtCore.QRect(410, 60, 81, 20))
        self.line_17.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_17.setLineWidth(3)
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setObjectName("line_17")
        self.label = QtWidgets.QLabel(self.groupBox_valve)
        self.label.setGeometry(QtCore.QRect(160, 60, 251, 51))
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setPixmap(QtGui.QPixmap(":/logo_vessel/resource/psavessel.png"))
        self.label.setObjectName("label")
        self.line_14 = QtWidgets.QFrame(self.groupBox_valve)
        self.line_14.setGeometry(QtCore.QRect(160, 110, 20, 61))
        self.line_14.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_14.setLineWidth(3)
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setObjectName("line_14")
        self.line_18 = QtWidgets.QFrame(self.groupBox_valve)
        self.line_18.setGeometry(QtCore.QRect(370, 230, 81, 20))
        self.line_18.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_18.setLineWidth(3)
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setObjectName("line_18")
        self.line = QtWidgets.QFrame(self.groupBox_valve)
        self.line.setGeometry(QtCore.QRect(20, 80, 491, 20))
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
        self.line_2 = QtWidgets.QFrame(self.groupBox_valve)
        self.line_2.setGeometry(QtCore.QRect(40, 340, 471, 20))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.BTN_PROD_PSA1 = QtWidgets.QPushButton(self.groupBox_valve)
        self.BTN_PROD_PSA1.setGeometry(QtCore.QRect(400, 150, 40, 40))
        self.BTN_PROD_PSA1.setIcon(icon)
        self.BTN_PROD_PSA1.setIconSize(QtCore.QSize(32, 32))
        self.BTN_PROD_PSA1.setCheckable(True)
        self.BTN_PROD_PSA1.setObjectName("BTN_PROD_PSA1")
        self.line_19 = QtWidgets.QFrame(self.groupBox_valve)
        self.line_19.setGeometry(QtCore.QRect(490, 230, 51, 20))
        self.line_19.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_19.setLineWidth(3)
        self.line_19.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_19.setObjectName("line_19")
        self.BTN_PSA1_PRO = QtWidgets.QPushButton(self.groupBox_valve)
        self.BTN_PSA1_PRO.setGeometry(QtCore.QRect(80, 140, 40, 40))
        self.BTN_PSA1_PRO.setIcon(icon)
        self.BTN_PSA1_PRO.setIconSize(QtCore.QSize(32, 32))
        self.BTN_PSA1_PRO.setCheckable(True)
        self.BTN_PSA1_PRO.setObjectName("BTN_PSA1_PRO")
        self.valveControlBackground = QtWidgets.QGraphicsView(self.groupBox_valve)
        self.valveControlBackground.setGeometry(QtCore.QRect(0, 20, 551, 401))
        self.valveControlBackground.setFrameShape(QtWidgets.QFrame.Panel)
        self.valveControlBackground.setFrameShadow(QtWidgets.QFrame.Plain)
        self.valveControlBackground.setObjectName("valveControlBackground")
        self.valveControlBackground.raise_()
        self.line_9.raise_()
        self.line_2.raise_()
        self.line_10.raise_()
        self.line.raise_()
        self.BTN_COL2_IN.raise_()
        self.BTN_PSA2_PRO.raise_()
        self.line_11.raise_()
        self.line_16.raise_()
        self.line_13.raise_()
        self.PROD.raise_()
        self.line_7.raise_()
        self.graphicsView.raise_()
        self.line_6.raise_()
        self.line_15.raise_()
        self.line_4.raise_()
        self.BTN_PSA2_IN.raise_()
        self.line_12.raise_()
        self.BTN_PSA2_BAL.raise_()
        self.BTN_PSA1_BAL.raise_()
        self.BTN_PSA2_CLR.raise_()
        self.BTN_PROD_OUT.raise_()
        self.BTN_PROD_PSA2.raise_()
        self.graphicsView_2.raise_()
        self.BTN_PSA1_IN.raise_()
        self.line_3.raise_()
        self.line_8.raise_()
        self.line_5.raise_()
        self.BTN_PSA1_CLR.raise_()
        self.line_17.raise_()
        self.label.raise_()
        self.line_14.raise_()
        self.line_18.raise_()
        self.BTN_PROD_PSA1.raise_()
        self.line_19.raise_()
        self.BTN_PSA1_PRO.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.frameSidePanel = QtWidgets.QFrame(self.centralwidget)
        self.frameSidePanel.setGeometry(QtCore.QRect(600, 10, 201, 441))
        self.frameSidePanel.setFrameShape(QtWidgets.QFrame.Box)
        self.frameSidePanel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameSidePanel.setLineWidth(2)
        self.frameSidePanel.setObjectName("frameSidePanel")
        self.groupBox_Condition = QtWidgets.QGroupBox(self.frameSidePanel)
        self.groupBox_Condition.setGeometry(QtCore.QRect(10, 10, 181, 191))
        self.groupBox_Condition.setObjectName("groupBox_Condition")
        self.label_5 = QtWidgets.QLabel(self.groupBox_Condition)
        self.label_5.setGeometry(QtCore.QRect(10, 21, 81, 20))
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.groupBox_Condition)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 51, 16))
        self.label_4.setObjectName("label_4")
        self.lcdTIME = QtWidgets.QLCDNumber(self.groupBox_Condition)
        self.lcdTIME.setGeometry(QtCore.QRect(10, 90, 161, 41))
        self.lcdTIME.setFrameShape(QtWidgets.QFrame.Panel)
        self.lcdTIME.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdTIME.setLineWidth(2)
        self.lcdTIME.setObjectName("lcdTIME")
        self.labelControlState = QtWidgets.QLabel(self.groupBox_Condition)
        self.labelControlState.setGeometry(QtCore.QRect(10, 40, 161, 21))
        self.labelControlState.setFrameShape(QtWidgets.QFrame.Panel)
        self.labelControlState.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelControlState.setLineWidth(2)
        self.labelControlState.setText("")
        self.labelControlState.setObjectName("labelControlState")
        self.label_6 = QtWidgets.QLabel(self.groupBox_Condition)
        self.label_6.setGeometry(QtCore.QRect(10, 140, 81, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_Condition)
        self.label_7.setGeometry(QtCore.QRect(100, 140, 71, 16))
        self.label_7.setObjectName("label_7")
        self.label_statePSA1 = QtWidgets.QLabel(self.groupBox_Condition)
        self.label_statePSA1.setGeometry(QtCore.QRect(10, 160, 71, 21))
        self.label_statePSA1.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_statePSA1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_statePSA1.setLineWidth(2)
        self.label_statePSA1.setText("")
        self.label_statePSA1.setObjectName("label_statePSA1")
        self.label_statePSA2 = QtWidgets.QLabel(self.groupBox_Condition)
        self.label_statePSA2.setGeometry(QtCore.QRect(100, 160, 71, 21))
        self.label_statePSA2.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_statePSA2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_statePSA2.setLineWidth(2)
        self.label_statePSA2.setText("")
        self.label_statePSA2.setObjectName("label_statePSA2")
        self.groupBox_ValveList = QtWidgets.QGroupBox(self.frameSidePanel)
        self.groupBox_ValveList.setGeometry(QtCore.QRect(10, 220, 181, 211))
        self.groupBox_ValveList.setObjectName("groupBox_ValveList")
        self.table_ValveList = QtWidgets.QTableWidget(self.groupBox_ValveList)
        self.table_ValveList.setGeometry(QtCore.QRect(0, 20, 181, 261))
        self.table_ValveList.setObjectName("table_ValveList")
        self.table_ValveList.setColumnCount(1)
        self.table_ValveList.setRowCount(15)
        item = QtWidgets.QTableWidgetItem()
        self.table_ValveList.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ValveList.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ValveList.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ValveList.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ValveList.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ValveList.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ValveList.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ValveList.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ValveList.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ValveList.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ValveList.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ValveList.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ValveList.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ValveList.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ValveList.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ValveList.setHorizontalHeaderItem(0, item)
        self.Background.raise_()
        self.frameSidePanel.raise_()
        self.frameBTNPanel.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 810, 18))
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
        self.actionRun = QtWidgets.QAction(MainWindow)
        self.actionRun.setObjectName("actionRun")
        self.actionPause = QtWidgets.QAction(MainWindow)
        self.actionPause.setObjectName("actionPause")
        self.menuAuto.addAction(self.actionStart)
        self.menuAuto.addAction(self.actionRepeat)
        self.menuControl.addAction(self.actionRun)
        self.menuControl.addAction(self.menuAuto.menuAction())
        self.menuControl.addAction(self.actionManual)
        self.menuControl.addAction(self.actionPause)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuControl.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setToolTip(_translate("MainWindow", "PSA1_PRO"))
        self.groupBox_valve.setTitle(_translate("MainWindow", "Valve control pannel"))
        self.BTN_COL2_IN.setToolTip(_translate("MainWindow", "COL2_IN"))
        self.BTN_PSA2_PRO.setToolTip(_translate("MainWindow", "PSA2_PRO"))
        self.BTN_PSA2_IN.setToolTip(_translate("MainWindow", "PSA2_IN"))
        self.BTN_PSA2_BAL.setToolTip(_translate("MainWindow", "PSA2_BAL"))
        self.BTN_PSA1_BAL.setToolTip(_translate("MainWindow", "PSA1_BAL"))
        self.BTN_PSA2_CLR.setToolTip(_translate("MainWindow", "PSA2_CLR"))
        self.BTN_PROD_OUT.setToolTip(_translate("MainWindow", "PROD_OUT"))
        self.BTN_PROD_PSA2.setToolTip(_translate("MainWindow", "PROD_PSA2"))
        self.BTN_PSA1_IN.setToolTip(_translate("MainWindow", "PSA1_IN"))
        self.BTN_PSA1_CLR.setToolTip(_translate("MainWindow", "PSA1_CLR"))
        self.BTN_PROD_PSA1.setToolTip(_translate("MainWindow", "PROD_PSA1"))
        self.BTN_PSA1_PRO.setToolTip(_translate("MainWindow", "PSA1_PRO"))
        self.groupBox_Condition.setTitle(_translate("MainWindow", "Working condition"))
        self.label_5.setText(_translate("MainWindow", "Control State"))
        self.label_4.setText(_translate("MainWindow", "Time [s]"))
        self.label_6.setText(_translate("MainWindow", "PSA1"))
        self.label_7.setText(_translate("MainWindow", "PSA2"))
        self.groupBox_ValveList.setTitle(_translate("MainWindow", "Valve list"))
        item = self.table_ValveList.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "PSA1_IN"))
        item = self.table_ValveList.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "PSA1_PRO"))
        item = self.table_ValveList.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "PSA1_BAL"))
        item = self.table_ValveList.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "PSA1_CLR"))
        item = self.table_ValveList.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "PSA2_IN"))
        item = self.table_ValveList.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "PSA2_PRO"))
        item = self.table_ValveList.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "PSA2_BAL"))
        item = self.table_ValveList.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "PSA2_CLR"))
        item = self.table_ValveList.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "PROD_OUT"))
        item = self.table_ValveList.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "PROD_PSA1"))
        item = self.table_ValveList.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "PROD_PSA2"))
        item = self.table_ValveList.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "COL2_IN"))
        item = self.table_ValveList.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.table_ValveList.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.table_ValveList.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.table_ValveList.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "STATE"))
        self.menuControl.setTitle(_translate("MainWindow", "Control"))
        self.menuAuto.setTitle(_translate("MainWindow", "Auto"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionManual.setText(_translate("MainWindow", "Manual"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionStart.setText(_translate("MainWindow", "Start"))
        self.actionRepeat.setText(_translate("MainWindow", "Repeat"))
        self.actionRun.setText(_translate("MainWindow", "Run"))
        self.actionPause.setText(_translate("MainWindow", "Pause"))
import res_rc
