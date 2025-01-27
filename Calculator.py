# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiCalculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(304, 495)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.resultText = QtWidgets.QLabel(self.centralwidget)
        self.resultText.setGeometry(QtCore.QRect(0, 0, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.resultText.setFont(font)
        self.resultText.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.resultText.setMidLineWidth(1)
        self.resultText.setTextFormat(QtCore.Qt.RichText)
        self.resultText.setObjectName("resultText")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 120, 2, 2))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 40, 301, 102))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_1 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_1.setMinimumSize(QtCore.QSize(50, 80))
        self.pushButton_1.setStyleSheet("background-color: rgb(255, 228, 23);\n"
"background-color: rgb(255, 183, 15);")
        self.pushButton_1.setObjectName("pushButton_1")
        self.horizontalLayout.addWidget(self.pushButton_1)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(50, 80))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 228, 23);\n"
"background-color: rgb(255, 183, 15);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton3.setMinimumSize(QtCore.QSize(50, 80))
        self.pushButton3.setStyleSheet("background-color: rgb(255, 228, 23);\n"
"background-color: rgb(255, 183, 15);")
        self.pushButton3.setObjectName("pushButton3")
        self.horizontalLayout.addWidget(self.pushButton3)
        self.plus = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.plus.setMinimumSize(QtCore.QSize(50, 80))
        self.plus.setStyleSheet("background-color: rgb(255, 228, 23);\n"
"background-color: rgb(255, 183, 15);")
        self.plus.setObjectName("plus")
        self.horizontalLayout.addWidget(self.plus)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 140, 301, 102))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_4.setMinimumSize(QtCore.QSize(50, 80))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 228, 23);\n"
"background-color: rgb(255, 183, 15);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_5.setMinimumSize(QtCore.QSize(50, 80))
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 228, 23);\n"
"background-color: rgb(255, 183, 15);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_6.setMinimumSize(QtCore.QSize(50, 80))
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 228, 23);\n"
"background-color: rgb(255, 183, 15);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.minus = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.minus.setMinimumSize(QtCore.QSize(50, 80))
        self.minus.setStyleSheet("background-color: rgb(255, 228, 23);\n"
"background-color: rgb(255, 183, 15);")
        self.minus.setObjectName("minus")
        self.horizontalLayout_2.addWidget(self.minus)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 240, 301, 102))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_7.setMinimumSize(QtCore.QSize(50, 80))
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 228, 23);\n"
"background-color: rgb(255, 183, 15);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_3.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_8.setMinimumSize(QtCore.QSize(50, 80))
        self.pushButton_8.setStyleSheet("background-color: rgb(255, 228, 23);\n"
"background-color: rgb(255, 183, 15);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_3.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_9.setMinimumSize(QtCore.QSize(50, 80))
        self.pushButton_9.setStyleSheet("background-color: rgb(255, 228, 23);\n"
"background-color: rgb(255, 183, 15);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_3.addWidget(self.pushButton_9)
        self.dived = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.dived.setMinimumSize(QtCore.QSize(50, 80))
        self.dived.setStyleSheet("background-color: rgb(255, 228, 23);\n"
"background-color: rgb(255, 183, 15);")
        self.dived.setObjectName("dived")
        self.horizontalLayout_3.addWidget(self.dived)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 340, 301, 102))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_Clean = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_Clean.setMinimumSize(QtCore.QSize(50, 80))
        self.pushButton_Clean.setStyleSheet("background-color: rgb(255, 228, 23);\n"
"background-color: rgb(255, 183, 15);")
        self.pushButton_Clean.setObjectName("pushButton_Clean")
        self.horizontalLayout_4.addWidget(self.pushButton_Clean)
        self.pushButton_Zero = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_Zero.setMinimumSize(QtCore.QSize(50, 80))
        self.pushButton_Zero.setStyleSheet("background-color: rgb(255, 228, 23);\n"
"background-color: rgb(255, 183, 15);")
        self.pushButton_Zero.setObjectName("pushButton_Zero")
        self.horizontalLayout_4.addWidget(self.pushButton_Zero)
        self.equal = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.equal.setMinimumSize(QtCore.QSize(50, 80))
        self.equal.setStyleSheet("background-color: rgb(255, 228, 23);\n"
"background-color: rgb(255, 183, 15);")
        self.equal.setObjectName("equal")
        self.horizontalLayout_4.addWidget(self.equal)
        self.multiply = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.multiply.setMinimumSize(QtCore.QSize(50, 80))
        self.multiply.setStyleSheet("background-color: rgb(255, 228, 23);\n"
"background-color: rgb(255, 183, 15);")
        self.multiply.setObjectName("multiply")
        self.horizontalLayout_4.addWidget(self.multiply)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 304, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.resultText.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton3.setText(_translate("MainWindow", "3"))
        self.plus.setText(_translate("MainWindow", "+"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.minus.setText(_translate("MainWindow", "-"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.dived.setText(_translate("MainWindow", "//"))
        self.pushButton_Clean.setText(_translate("MainWindow", "R"))
        self.pushButton_Zero.setText(_translate("MainWindow", "0"))
        self.equal.setText(_translate("MainWindow", "="))
        self.multiply.setText(_translate("MainWindow", "*"))
