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
        self.action_page = QtWidgets.QWidget()
        self.action_page.setObjectName("action_page")
        self.action_frame = QtWidgets.QFrame(self.action_page)
        self.action_frame.setGeometry(QtCore.QRect(0, -10, 581, 481))
        self.action_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.action_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.action_frame.setObjectName("action_frame")
        self.action = QtWidgets.QTableWidget(self.action_frame)
        self.action.setGeometry(QtCore.QRect(0, 10, 581, 281))
        self.action.setObjectName("action")
        self.action.setColumnCount(5)
        self.action.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.action.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.action.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.action.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.action.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.action.setHorizontalHeaderItem(4, item)
        self.add_new_note = QtWidgets.QPushButton(self.action_frame)
        self.add_new_note.setGeometry(QtCore.QRect(140, 290, 101, 23))
        self.add_new_note.setObjectName("add_new_note")
        self.edit_selected = QtWidgets.QPushButton(self.action_frame)
        self.edit_selected.setGeometry(QtCore.QRect(250, 290, 131, 23))
        self.edit_selected.setObjectName("edit_selected")
        self.delete_selected = QtWidgets.QPushButton(self.action_frame)
        self.delete_selected.setGeometry(QtCore.QRect(140, 320, 241, 23))
        self.delete_selected.setObjectName("delete_selected")
        self.stackedWidget.addWidget(self.action_page)
        self.client_page = QtWidgets.QWidget()
        self.client_page.setObjectName("client_page")
        self.client_frame = QtWidgets.QFrame(self.client_page)
        self.client_frame.setGeometry(QtCore.QRect(0, 0, 571, 341))
        self.client_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.client_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.client_frame.setObjectName("client_frame")
        self.client_name_line_Edit = QtWidgets.QLineEdit(self.client_frame)
        self.client_name_line_Edit.setGeometry(QtCore.QRect(20, 30, 113, 20))
        self.client_name_line_Edit.setObjectName("client_name_line_Edit")
        self.label = QtWidgets.QLabel(self.client_frame)
        self.label.setGeometry(QtCore.QRect(20, 3, 81, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.client_frame)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 121, 16))
        self.label_2.setObjectName("label_2")
        self.client_second_name_line_Edit = QtWidgets.QLineEdit(self.client_frame)
        self.client_second_name_line_Edit.setGeometry(QtCore.QRect(20, 80, 113, 20))
        self.client_second_name_line_Edit.setObjectName("client_second_name_line_Edit")
        self.label_3 = QtWidgets.QLabel(self.client_frame)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 111, 16))
        self.label_3.setObjectName("label_3")
        self.client_age_line_Edit = QtWidgets.QLineEdit(self.client_frame)
        self.client_age_line_Edit.setGeometry(QtCore.QRect(20, 130, 113, 20))
        self.client_age_line_Edit.setObjectName("client_age_line_Edit")
        self.type_of_visit_radioButton1 = QtWidgets.QRadioButton(self.client_frame)
        self.type_of_visit_radioButton1.setGeometry(QtCore.QRect(20, 160, 111, 21))
        self.type_of_visit_radioButton1.setObjectName("type_of_visit_radioButton1")
        self.type_of_visit_radioButton2 = QtWidgets.QRadioButton(self.client_frame)
        self.type_of_visit_radioButton2.setGeometry(QtCore.QRect(20, 190, 111, 21))
        self.type_of_visit_radioButton2.setObjectName("type_of_visit_radioButton2")
        self.add_client = QtWidgets.QPushButton(self.client_frame)
        self.add_client.setGeometry(QtCore.QRect(20, 220, 75, 23))
        self.add_client.setObjectName("add_client")
        self.client_comboBox = QtWidgets.QComboBox(self.client_frame)
        self.client_comboBox.setGeometry(QtCore.QRect(370, 40, 181, 22))
        self.client_comboBox.setObjectName("client_comboBox")
        self.label_4 = QtWidgets.QLabel(self.client_frame)
        self.label_4.setGeometry(QtCore.QRect(370, 20, 151, 16))
        self.label_4.setObjectName("label_4")
        self.client_clear = QtWidgets.QPushButton(self.client_frame)
        self.client_clear.setGeometry(QtCore.QRect(20, 250, 75, 23))
        self.client_clear.setObjectName("client_clear")
        self.cancel_client = QtWidgets.QPushButton(self.client_frame)
        self.cancel_client.setGeometry(QtCore.QRect(20, 280, 75, 23))
        self.cancel_client.setObjectName("cancel_client")
        self.to_officer = QtWidgets.QPushButton(self.client_frame)
        self.to_officer.setGeometry(QtCore.QRect(20, 310, 75, 23))
        self.to_officer.setObjectName("to_officer")
        self.stackedWidget.addWidget(self.client_page)
        self.officer_page = QtWidgets.QWidget()
        self.officer_page.setObjectName("officer_page")
        self.officer_frame = QtWidgets.QFrame(self.officer_page)
        self.officer_frame.setGeometry(QtCore.QRect(0, 0, 581, 381))
        self.officer_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.officer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.officer_frame.setObjectName("officer_frame")
        self.officer_comboBox = QtWidgets.QComboBox(self.officer_frame)
        self.officer_comboBox.setGeometry(QtCore.QRect(410, 30, 161, 22))
        self.officer_comboBox.setObjectName("officer_comboBox")
        self.label_5 = QtWidgets.QLabel(self.officer_frame)
        self.label_5.setGeometry(QtCore.QRect(410, 10, 161, 16))
        self.label_5.setObjectName("label_5")
        self.officer_name_lineEdit = QtWidgets.QLineEdit(self.officer_frame)
        self.officer_name_lineEdit.setGeometry(QtCore.QRect(10, 30, 81, 20))
        self.officer_name_lineEdit.setObjectName("officer_name_lineEdit")
        self.label_6 = QtWidgets.QLabel(self.officer_frame)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 81, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.officer_frame)
        self.label_7.setGeometry(QtCore.QRect(10, 60, 121, 16))
        self.label_7.setObjectName("label_7")
        self.officer_second_name_lineEdit = QtWidgets.QLineEdit(self.officer_frame)
        self.officer_second_name_lineEdit.setGeometry(QtCore.QRect(10, 80, 111, 20))
        self.officer_second_name_lineEdit.setObjectName("officer_second_name_lineEdit")
        self.label_8 = QtWidgets.QLabel(self.officer_frame)
        self.label_8.setGeometry(QtCore.QRect(10, 110, 81, 16))
        self.label_8.setObjectName("label_8")
        self.officer_age_lineEdit = QtWidgets.QLineEdit(self.officer_frame)
        self.officer_age_lineEdit.setGeometry(QtCore.QRect(10, 130, 71, 20))
        self.officer_age_lineEdit.setObjectName("officer_age_lineEdit")
        self.label_9 = QtWidgets.QLabel(self.officer_frame)
        self.label_9.setGeometry(QtCore.QRect(10, 160, 91, 16))
        self.label_9.setObjectName("label_9")
        self.work_exeperience_lineEdit = QtWidgets.QLineEdit(self.officer_frame)
        self.work_exeperience_lineEdit.setGeometry(QtCore.QRect(10, 180, 81, 20))
        self.work_exeperience_lineEdit.setObjectName("work_exeperience_lineEdit")
        self.label_10 = QtWidgets.QLabel(self.officer_frame)
        self.label_10.setGeometry(QtCore.QRect(10, 210, 81, 16))
        self.label_10.setObjectName("label_10")
        self.work_schedule_lineEdit = QtWidgets.QLineEdit(self.officer_frame)
        self.work_schedule_lineEdit.setGeometry(QtCore.QRect(10, 230, 81, 20))
        self.work_schedule_lineEdit.setObjectName("work_schedule_lineEdit")
        self.add_officer = QtWidgets.QPushButton(self.officer_frame)
        self.add_officer.setGeometry(QtCore.QRect(10, 260, 75, 23))
        self.add_officer.setObjectName("add_officer")
        self.clear_officer = QtWidgets.QPushButton(self.officer_frame)
        self.clear_officer.setGeometry(QtCore.QRect(10, 290, 75, 23))
        self.clear_officer.setObjectName("clear_officer")
        self.cancel_officer = QtWidgets.QPushButton(self.officer_frame)
        self.cancel_officer.setGeometry(QtCore.QRect(10, 320, 75, 23))
        self.cancel_officer.setObjectName("cancel_officer")
        self.to_wepon = QtWidgets.QPushButton(self.officer_frame)
        self.to_wepon.setGeometry(QtCore.QRect(90, 260, 75, 23))
        self.to_wepon.setObjectName("to_wepon")
        self.back_to_client = QtWidgets.QPushButton(self.officer_frame)
        self.back_to_client.setGeometry(QtCore.QRect(90, 320, 91, 23))
        self.back_to_client.setObjectName("back_to_client")
        self.stackedWidget.addWidget(self.officer_page)
        self.wepon_page = QtWidgets.QWidget()
        self.wepon_page.setObjectName("wepon_page")
        self.wepon_frame = QtWidgets.QFrame(self.wepon_page)
        self.wepon_frame.setGeometry(QtCore.QRect(0, 10, 581, 361))
        self.wepon_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.wepon_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.wepon_frame.setObjectName("wepon_frame")
        self.wepon_comboBox = QtWidgets.QComboBox(self.wepon_frame)
        self.wepon_comboBox.setGeometry(QtCore.QRect(400, 30, 161, 22))
        self.wepon_comboBox.setObjectName("wepon_comboBox")
        self.label_11 = QtWidgets.QLabel(self.wepon_frame)
        self.label_11.setGeometry(QtCore.QRect(400, 10, 161, 20))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.wepon_frame)
        self.label_12.setGeometry(QtCore.QRect(20, 20, 81, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.wepon_frame)
        self.label_13.setGeometry(QtCore.QRect(20, 60, 111, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.wepon_frame)
        self.label_14.setGeometry(QtCore.QRect(20, 100, 111, 16))
        self.label_14.setObjectName("label_14")
        self.action_radioButton1 = QtWidgets.QRadioButton(self.wepon_frame)
        self.action_radioButton1.setGeometry(QtCore.QRect(20, 150, 82, 17))
        self.action_radioButton1.setObjectName("action_radioButton1")
        self.action_radioButton2 = QtWidgets.QRadioButton(self.wepon_frame)
        self.action_radioButton2.setGeometry(QtCore.QRect(20, 170, 82, 17))
        self.action_radioButton2.setObjectName("action_radioButton2")
        self.wepon_mark_lineEdit = QtWidgets.QLineEdit(self.wepon_frame)
        self.wepon_mark_lineEdit.setGeometry(QtCore.QRect(20, 40, 113, 20))
        self.wepon_mark_lineEdit.setObjectName("wepon_mark_lineEdit")
        self.wepon_calibr_lineEdit = QtWidgets.QLineEdit(self.wepon_frame)
        self.wepon_calibr_lineEdit.setGeometry(QtCore.QRect(20, 80, 113, 20))
        self.wepon_calibr_lineEdit.setObjectName("wepon_calibr_lineEdit")
        self.wepon_ammo_lineEdit = QtWidgets.QLineEdit(self.wepon_frame)
        self.wepon_ammo_lineEdit.setGeometry(QtCore.QRect(20, 120, 113, 20))
        self.wepon_ammo_lineEdit.setObjectName("wepon_ammo_lineEdit")
        self.add_wepon = QtWidgets.QPushButton(self.wepon_frame)
        self.add_wepon.setGeometry(QtCore.QRect(20, 200, 75, 23))
        self.add_wepon.setObjectName("add_wepon")
        self.clear_wepon = QtWidgets.QPushButton(self.wepon_frame)
        self.clear_wepon.setGeometry(QtCore.QRect(20, 230, 75, 23))
        self.clear_wepon.setObjectName("clear_wepon")
        self.cancel_wepon = QtWidgets.QPushButton(self.wepon_frame)
        self.cancel_wepon.setGeometry(QtCore.QRect(20, 260, 75, 23))
        self.cancel_wepon.setObjectName("cancel_wepon")
        self.back_to_officer = QtWidgets.QPushButton(self.wepon_frame)
        self.back_to_officer.setGeometry(QtCore.QRect(110, 200, 91, 23))
        self.back_to_officer.setObjectName("back_to_officer")
        self.to_list_upgrades = QtWidgets.QPushButton(self.wepon_frame)
        self.to_list_upgrades.setGeometry(QtCore.QRect(110, 260, 101, 23))
        self.to_list_upgrades.setObjectName("to_list_upgrades")
        self.stackedWidget.addWidget(self.wepon_page)
        self.upgrade_page = QtWidgets.QWidget()
        self.upgrade_page.setObjectName("upgrade_page")
        self.upgrade_frame = QtWidgets.QFrame(self.upgrade_page)
        self.upgrade_frame.setGeometry(QtCore.QRect(10, 10, 561, 361))
        self.upgrade_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.upgrade_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.upgrade_frame.setObjectName("upgrade_frame")
        self.label_15 = QtWidgets.QLabel(self.upgrade_frame)
        self.label_15.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.label_15.setObjectName("label_15")
        self.upgrades_comboBox = QtWidgets.QComboBox(self.upgrade_frame)
        self.upgrades_comboBox.setGeometry(QtCore.QRect(350, 30, 201, 22))
        self.upgrades_comboBox.setObjectName("upgrades_comboBox")
        self.upgrades_scope_lineEdit = QtWidgets.QLineEdit(self.upgrade_frame)
        self.upgrades_scope_lineEdit.setGeometry(QtCore.QRect(10, 30, 113, 20))
        self.upgrades_scope_lineEdit.setObjectName("upgrades_scope_lineEdit")
        self.label_16 = QtWidgets.QLabel(self.upgrade_frame)
        self.label_16.setGeometry(QtCore.QRect(350, 10, 201, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.upgrade_frame)
        self.label_17.setGeometry(QtCore.QRect(10, 60, 47, 13))
        self.label_17.setObjectName("label_17")
        self.upgrades_handle_lineEdit = QtWidgets.QLineEdit(self.upgrade_frame)
        self.upgrades_handle_lineEdit.setGeometry(QtCore.QRect(10, 80, 113, 20))
        self.upgrades_handle_lineEdit.setObjectName("upgrades_handle_lineEdit")
        self.label_18 = QtWidgets.QLabel(self.upgrade_frame)
        self.label_18.setGeometry(QtCore.QRect(10, 110, 71, 16))
        self.label_18.setObjectName("label_18")
        self.upgrade_mag_lineEdit = QtWidgets.QLineEdit(self.upgrade_frame)
        self.upgrade_mag_lineEdit.setGeometry(QtCore.QRect(10, 130, 113, 20))
        self.upgrade_mag_lineEdit.setObjectName("upgrade_mag_lineEdit")
        self.label_19 = QtWidgets.QLabel(self.upgrade_frame)
        self.label_19.setGeometry(QtCore.QRect(10, 160, 71, 16))
        self.label_19.setObjectName("label_19")
        self.upgrades_type_of_mag_lineEdit = QtWidgets.QLineEdit(self.upgrade_frame)
        self.upgrades_type_of_mag_lineEdit.setGeometry(QtCore.QRect(10, 180, 113, 20))
        self.upgrades_type_of_mag_lineEdit.setObjectName("upgrades_type_of_mag_lineEdit")
        self.label_20 = QtWidgets.QLabel(self.upgrade_frame)
        self.label_20.setGeometry(QtCore.QRect(10, 210, 81, 16))
        self.label_20.setObjectName("label_20")
        self.upgrade_type_of_ammo_lineEdit = QtWidgets.QLineEdit(self.upgrade_frame)
        self.upgrade_type_of_ammo_lineEdit.setGeometry(QtCore.QRect(10, 230, 113, 20))
        self.upgrade_type_of_ammo_lineEdit.setObjectName("upgrade_type_of_ammo_lineEdit")
        self.add_list_of_upgrades = QtWidgets.QPushButton(self.upgrade_frame)
        self.add_list_of_upgrades.setGeometry(QtCore.QRect(10, 260, 121, 23))
        self.add_list_of_upgrades.setObjectName("add_list_of_upgrades")
        self.clear_upgrade = QtWidgets.QPushButton(self.upgrade_frame)
        self.clear_upgrade.setGeometry(QtCore.QRect(10, 290, 121, 23))
        self.clear_upgrade.setObjectName("clear_upgrade")
        self.cancel_upgrade = QtWidgets.QPushButton(self.upgrade_frame)
        self.cancel_upgrade.setGeometry(QtCore.QRect(10, 320, 121, 23))
        self.cancel_upgrade.setObjectName("cancel_upgrade")
        self.back_to_wepon = QtWidgets.QPushButton(self.upgrade_frame)
        self.back_to_wepon.setGeometry(QtCore.QRect(150, 260, 101, 23))
        self.back_to_wepon.setObjectName("back_to_wepon")
        self.to_list = QtWidgets.QPushButton(self.upgrade_frame)
        self.to_list.setGeometry(QtCore.QRect(160, 320, 75, 23))
        self.to_list.setObjectName("to_list")
        self.stackedWidget.addWidget(self.upgrade_page)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.action.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Client"))
        item = self.action.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Officer"))
        item = self.action.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Wepon"))
        item = self.action.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Action"))
        item = self.action.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Date"))
        self.add_new_note.setText(_translate("MainWindow", "Add a new note"))
        self.edit_selected.setText(_translate("MainWindow", "Edit selected note"))
        self.delete_selected.setText(_translate("MainWindow", "Delete selected note"))
        self.label.setText(_translate("MainWindow", "Name of client:"))
        self.label_2.setText(_translate("MainWindow", "Second name of client:"))
        self.label_3.setText(_translate("MainWindow", "Age of client:"))
        self.type_of_visit_radioButton1.setText(_translate("MainWindow", "Type of visit:One"))
        self.type_of_visit_radioButton2.setText(_translate("MainWindow", "Type of visit:All"))
        self.add_client.setText(_translate("MainWindow", "Add client"))
        self.label_4.setText(_translate("MainWindow", "Chousing client from database:"))
        self.client_clear.setText(_translate("MainWindow", "Clear all"))
        self.cancel_client.setText(_translate("MainWindow", "Cancel"))
        self.to_officer.setText(_translate("MainWindow", "To Officer"))
        self.label_5.setText(_translate("MainWindow", "Chousing officer from database:"))
        self.label_6.setText(_translate("MainWindow", "Name of officer:"))
        self.label_7.setText(_translate("MainWindow", "Second name of officer:"))
        self.label_8.setText(_translate("MainWindow", "Age of officer:"))
        self.label_9.setText(_translate("MainWindow", "Work experience:"))
        self.label_10.setText(_translate("MainWindow", "Work schedule:"))
        self.add_officer.setText(_translate("MainWindow", "Add officer"))
        self.clear_officer.setText(_translate("MainWindow", "Clear all"))
        self.cancel_officer.setText(_translate("MainWindow", "Cancel"))
        self.to_wepon.setText(_translate("MainWindow", "To wepon"))
        self.back_to_client.setText(_translate("MainWindow", "Back to Client"))
        self.label_11.setText(_translate("MainWindow", "Chousing wepon from database:"))
        self.label_12.setText(_translate("MainWindow", "Mark of wepon:"))
        self.label_13.setText(_translate("MainWindow", "Calibr of wepon:"))
        self.label_14.setText(_translate("MainWindow", "Ammo taken:"))
        self.action_radioButton1.setText(_translate("MainWindow", "Given"))
        self.action_radioButton2.setText(_translate("MainWindow", "Backed"))
        self.add_wepon.setText(_translate("MainWindow", "Add wepon"))
        self.clear_wepon.setText(_translate("MainWindow", "Clear all"))
        self.cancel_wepon.setText(_translate("MainWindow", "Cancel"))
        self.back_to_officer.setText(_translate("MainWindow", "Back to officer"))
        self.to_list_upgrades.setText(_translate("MainWindow", "To list of upgrades"))
        self.label_15.setText(_translate("MainWindow", "Scope:"))
        self.label_16.setText(_translate("MainWindow", "Chouse list of upgrades from database:"))
        self.label_17.setText(_translate("MainWindow", "Handle:"))
        self.label_18.setText(_translate("MainWindow", "Mag:"))
        self.label_19.setText(_translate("MainWindow", "Type of mag:"))
        self.label_20.setText(_translate("MainWindow", "Type of ammo:"))
        self.add_list_of_upgrades.setText(_translate("MainWindow", "Add list of upgrades"))
        self.clear_upgrade.setText(_translate("MainWindow", "Clear all"))
        self.cancel_upgrade.setText(_translate("MainWindow", "Cancel"))
        self.back_to_wepon.setText(_translate("MainWindow", "Back to wepon"))
        self.to_list.setText(_translate("MainWindow", "To list "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
