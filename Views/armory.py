# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'armory.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(577, 377)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(-1, -1, 641, 461))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.frame = QtWidgets.QFrame(self.page)
        self.frame.setGeometry(QtCore.QRect(0, -10, 581, 481))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(0, 10, 581, 281))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(140, 290, 101, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 290, 131, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 320, 241, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.frame_2 = QtWidgets.QFrame(self.page_2)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 571, 341))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(20, 3, 81, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 121, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 80, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 111, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 130, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.radioButton = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton.setGeometry(QtCore.QRect(20, 160, 111, 21))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 190, 111, 21))
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 220, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setGeometry(QtCore.QRect(370, 40, 181, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(370, 20, 151, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 250, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 280, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 310, 75, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.frame_3 = QtWidgets.QFrame(self.page_3)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 581, 381))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_2.setGeometry(QtCore.QRect(410, 30, 161, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(410, 10, 161, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 30, 81, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 81, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(10, 60, 121, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 80, 111, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(10, 110, 81, 16))
        self.label_8.setObjectName("label_8")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(10, 130, 71, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setGeometry(QtCore.QRect(10, 160, 91, 16))
        self.label_9.setObjectName("label_9")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(10, 180, 81, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(10, 210, 81, 16))
        self.label_10.setObjectName("label_10")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_8.setGeometry(QtCore.QRect(10, 230, 81, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 260, 75, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 290, 75, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_10.setGeometry(QtCore.QRect(10, 320, 75, 23))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_11.setGeometry(QtCore.QRect(90, 260, 75, 23))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_12.setGeometry(QtCore.QRect(90, 320, 91, 23))
        self.pushButton_12.setObjectName("pushButton_12")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.frame_4 = QtWidgets.QFrame(self.page_4)
        self.frame_4.setGeometry(QtCore.QRect(0, 10, 581, 361))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_3.setGeometry(QtCore.QRect(400, 30, 161, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_11 = QtWidgets.QLabel(self.frame_4)
        self.label_11.setGeometry(QtCore.QRect(400, 10, 161, 20))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame_4)
        self.label_12.setGeometry(QtCore.QRect(20, 20, 81, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_4)
        self.label_13.setGeometry(QtCore.QRect(20, 60, 111, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame_4)
        self.label_14.setGeometry(QtCore.QRect(20, 100, 111, 16))
        self.label_14.setObjectName("label_14")
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 150, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_4.setGeometry(QtCore.QRect(20, 170, 82, 17))
        self.radioButton_4.setObjectName("radioButton_4")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_9.setGeometry(QtCore.QRect(20, 40, 113, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_10.setGeometry(QtCore.QRect(20, 80, 113, 20))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_11.setGeometry(QtCore.QRect(20, 120, 113, 20))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_13.setGeometry(QtCore.QRect(20, 200, 75, 23))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_14.setGeometry(QtCore.QRect(20, 230, 75, 23))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_15.setGeometry(QtCore.QRect(20, 260, 75, 23))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_16.setGeometry(QtCore.QRect(110, 200, 91, 23))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_17.setGeometry(QtCore.QRect(110, 260, 101, 23))
        self.pushButton_17.setObjectName("pushButton_17")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.frame_5 = QtWidgets.QFrame(self.page_5)
        self.frame_5.setGeometry(QtCore.QRect(10, 10, 561, 361))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_15 = QtWidgets.QLabel(self.frame_5)
        self.label_15.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.label_15.setObjectName("label_15")
        self.comboBox_4 = QtWidgets.QComboBox(self.frame_5)
        self.comboBox_4.setGeometry(QtCore.QRect(350, 30, 201, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_12.setGeometry(QtCore.QRect(10, 30, 113, 20))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_16 = QtWidgets.QLabel(self.frame_5)
        self.label_16.setGeometry(QtCore.QRect(350, 10, 201, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.frame_5)
        self.label_17.setGeometry(QtCore.QRect(10, 60, 47, 13))
        self.label_17.setObjectName("label_17")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_13.setGeometry(QtCore.QRect(10, 80, 113, 20))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_18 = QtWidgets.QLabel(self.frame_5)
        self.label_18.setGeometry(QtCore.QRect(10, 110, 71, 16))
        self.label_18.setObjectName("label_18")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_14.setGeometry(QtCore.QRect(10, 130, 113, 20))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_19 = QtWidgets.QLabel(self.frame_5)
        self.label_19.setGeometry(QtCore.QRect(10, 160, 71, 16))
        self.label_19.setObjectName("label_19")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_15.setGeometry(QtCore.QRect(10, 180, 113, 20))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_20 = QtWidgets.QLabel(self.frame_5)
        self.label_20.setGeometry(QtCore.QRect(10, 210, 81, 16))
        self.label_20.setObjectName("label_20")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_16.setGeometry(QtCore.QRect(10, 230, 113, 20))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.pushButton_18 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_18.setGeometry(QtCore.QRect(10, 260, 121, 23))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_19.setGeometry(QtCore.QRect(10, 290, 121, 23))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_20.setGeometry(QtCore.QRect(10, 320, 121, 23))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_21.setGeometry(QtCore.QRect(150, 260, 101, 23))
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_22.setGeometry(QtCore.QRect(160, 320, 75, 23))
        self.pushButton_22.setObjectName("pushButton_22")
        self.stackedWidget.addWidget(self.page_5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Client"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Officer"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Wepon"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Action"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Date"))
        self.pushButton.setText(_translate("MainWindow", "Add a new note"))
        self.pushButton_2.setText(_translate("MainWindow", "Edit selected note"))
        self.pushButton_3.setText(_translate("MainWindow", "Delete selected note"))
        self.label.setText(_translate("MainWindow", "Name of client:"))
        self.label_2.setText(_translate("MainWindow", "Second name of client:"))
        self.label_3.setText(_translate("MainWindow", "Age of client:"))
        self.radioButton.setText(_translate("MainWindow", "Type of visit:One"))
        self.radioButton_2.setText(_translate("MainWindow", "Type of visit:All"))
        self.pushButton_4.setText(_translate("MainWindow", "Add client"))
        self.label_4.setText(_translate("MainWindow", "Chousing client from database:"))
        self.pushButton_5.setText(_translate("MainWindow", "Clear all"))
        self.pushButton_6.setText(_translate("MainWindow", "Cancel"))
        self.pushButton_7.setText(_translate("MainWindow", "To Officer"))
        self.label_5.setText(_translate("MainWindow", "Chousing officer from database:"))
        self.label_6.setText(_translate("MainWindow", "Name of officer:"))
        self.label_7.setText(_translate("MainWindow", "Second name of officer:"))
        self.label_8.setText(_translate("MainWindow", "Age of officer:"))
        self.label_9.setText(_translate("MainWindow", "Work experience:"))
        self.label_10.setText(_translate("MainWindow", "Work schedule:"))
        self.pushButton_8.setText(_translate("MainWindow", "Add officer"))
        self.pushButton_9.setText(_translate("MainWindow", "Clear all"))
        self.pushButton_10.setText(_translate("MainWindow", "Cancel"))
        self.pushButton_11.setText(_translate("MainWindow", "To wepon"))
        self.pushButton_12.setText(_translate("MainWindow", "Back to Client"))
        self.label_11.setText(_translate("MainWindow", "Chousing wepon from database:"))
        self.label_12.setText(_translate("MainWindow", "Mark of wepon:"))
        self.label_13.setText(_translate("MainWindow", "Calibr of wepon:"))
        self.label_14.setText(_translate("MainWindow", "Ammo taken:"))
        self.radioButton_3.setText(_translate("MainWindow", "Given"))
        self.radioButton_4.setText(_translate("MainWindow", "Backed"))
        self.pushButton_13.setText(_translate("MainWindow", "Add wepon"))
        self.pushButton_14.setText(_translate("MainWindow", "Clear all"))
        self.pushButton_15.setText(_translate("MainWindow", "Cancel"))
        self.pushButton_16.setText(_translate("MainWindow", "Back to officer"))
        self.pushButton_17.setText(_translate("MainWindow", "To list of upgrades"))
        self.label_15.setText(_translate("MainWindow", "Scope:"))
        self.label_16.setText(_translate("MainWindow", "Chouse list of upgrades from database:"))
        self.label_17.setText(_translate("MainWindow", "Handle:"))
        self.label_18.setText(_translate("MainWindow", "Mag:"))
        self.label_19.setText(_translate("MainWindow", "Type of mag:"))
        self.label_20.setText(_translate("MainWindow", "Type of ammo:"))
        self.pushButton_18.setText(_translate("MainWindow", "Add list of upgrades"))
        self.pushButton_19.setText(_translate("MainWindow", "Clear all"))
        self.pushButton_20.setText(_translate("MainWindow", "Cancel"))
        self.pushButton_21.setText(_translate("MainWindow", "Back to wepon"))
        self.pushButton_22.setText(_translate("MainWindow", "To list "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())