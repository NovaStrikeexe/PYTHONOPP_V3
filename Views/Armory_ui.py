from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMainWindow
from pony.orm import db_session

from Classes.Client import Client
from Classes.ShootingOfficer import ShootingOfficer
from Classes.Wepons import Wepons
from Classes.Cur_wepon import Cur_wepon
from Classes.Action import Action
from Classes.List_of_upgrades import List_of_upgrades
from Classes.OfficerClientWepon import OfficerClientWepon
from Views.armory import Ui_MainWindow

# Customer Variables
name_of_client = ""
second_name_of_client = ""
age_of_client = 0
type_of_visit = False
# Officer Variables
name_of_officer = ""
second_name_of_officer = ""
age_of_officer = 0
work_exp = ""
work_ckd = ""
# Wepon Variables
mark = ""
calibr = 0.0
ammo = 0
# Action Variable
status = False
# Upgrades Variables
scope = ""
handel = ""
mag = 0
type_of_mag = ""
type_of_bulets = ""


class Armory(QMainWindow):
    def __init__(self):
        super(Armory, self).__init__()
        self.initUI()

    def initUI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(580, 380)
        self.ui.stackedWidget.setCurrentIndex(0)
        # connection for events of frame action
        self.ui.add_new_note.clicked.connect(self.click_add_new_note)  #
        self.ui.delete_selected.clicked.connect(self.click_delete_selected)  #
        self.ui.edit_selected.clicked.connect(self.click_edit_selected)  #

        # connection for events of adding object of classes
        self.ui.add_client.clicked.connect(self.click_add_client)  #
        self.ui.add_officer.clicked.connect(self.click_add_officer)  #
        self.ui.add_wepon.clicked.connect(self.click_add_wepon)  #
        self.ui.add_list_of_upgrades.clicked.connect(self.click_add_list_of_upgrades)  #

        # connection for events with forms
        self.ui.to_officer.clicked.connect(self.click_to_officer)  #
        self.ui.to_wepon.clicked.connect(self.click_to_wepon)  #
        self.ui.to_list_upgrades.clicked.connect(self.click_to_list_upgrades)  #
        self.ui.to_list.clicked.connect(self.click_to_list)  #

        # connection for events clearing of lineEdits of classes
        self.ui.client_clear.clicked.connect(self.click_client_clear)  #
        self.ui.clear_officer.clicked.connect(self.click_clear_officer)  #
        self.ui.clear_wepon.clicked.connect(self.click_clear_wepon)  #
        self.ui.clear_upgrade.clicked.connect(self.click_clear_upgrade)  #

        # connection for evenet canceling of lineEdits of classes
        self.ui.cancel_client.clicked.connect(self.click_cancel_client)  #
        self.ui.cancel_officer.clicked.connect(self.click_cancel_officer)  #
        self.ui.cancel_wepon.clicked.connect(self.click_cancel_wepon)  #
        self.ui.cancel_upgrade.clicked.connect(self.click_cancel_upgrade)#

        # connection for backing to pages
        self.ui.back_to_client.clicked.connect(self.click_back_to_client)
        self.ui.back_to_officer.clicked.connect(self.click_back_to_officer)
        self.ui.back_to_wepon.clicked.connect(self.click_back_to_wepon)


        # validation of lineEdits of class Client fields
        self.ui.client_name_line_Edit.setValidator(QRegExpValidator(QRegExp("^[A-z][a-z]+$")))
        self.ui.client_second_name_line_Edit.setValidator((QRegExpValidator(QRegExp("^[A-z][a-z]+/-[A-z][a-z]+$"))))
        self.ui.client_age_line_Edit.setValidator((QRegExpValidator(QRegExp("^[0-9]+$"))))
        # validation of lineEdits of class Officer fields
        self.ui.officer_name_lineEdit.setValidator((QRegExpValidator(QRegExp("^[A-z][a-z]+$"))))
        self.ui.officer_second_name_lineEdit.setValidator((QRegExpValidator(QRegExp("^[A-z][a-z]+/-[A-z][a-z]+$"))))
        self.ui.officer_age_lineEdit.setValidator(QRegExpValidator(QRegExp("^[0-9]*$")))
        self.ui.work_exeperience_lineEdit.setValidator(QRegExpValidator(QRegExp("^[0-9-a-zA-Z]*$")))
        self.ui.work_schedule_lineEdit.setValidator(QRegExpValidator((QRegExp("^[0-9//0-9]*$"))))
        # validation of lineEdits of class Wepon fields
        self.ui.wepon_mark_lineEdit.setValidator(QRegExpValidator(QRegExp("^[0-9a-zA-Z/-]*$")))
        self.ui.wepon_calibr_lineEdit.setValidator(QRegExpValidator(QRegExp("^[0-9/.]*$")))
        self.ui.wepon_ammo_lineEdit.setValidator(QRegExpValidator(QRegExp("^[0-9]$")))

    def click_add_new_note(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def click_delete_selected(self):
        pass

    def click_edit_selected(self):
        pass

    def click_add_client(self):
        global name_of_client, second_name_of_client, age_of_client, type_of_visit
        name_of_client = self.ui.client_name_line_Edit.text()
        second_name_of_client = self.ui.client_second_name_line_Edit.text()
        age_of_client = self.ui.client_age_line_Edit.text()
        if self.ui.type_of_visit_radioButton1.isChecked():
            type_of_visit = True
        else:
            type_of_visit = False
        self.ui.client_name_line_Edit.clear()
        self.ui.client_second_name_line_Edit.clear()
        self.ui.client_age_line_Edit.clear()
        self.ui.type_of_visit_radioButton1.setChecked(False)
        self.ui.type_of_visit_radioButton2.setChecked(False)
        self.ui.type_of_visit_radioButton1.setDisabled(True)
        self.ui.type_of_visit_radioButton2.setDisabled(True)
        self.ui.client_comboBox.setDisabled(True)
        self.ui.add_client.setDisabled(True)
        self.ui.client_clear.setDisabled(True)

    def click_add_officer(self):
        global name_of_officer, second_name_of_officer, age_of_officer, work_exp, work_ckd
        name_of_officer = self.ui.officer_name_lineEdit.text()
        second_name_of_officer = self.ui.officer_second_name_lineEdit.text()
        age_of_officer = self.ui.officer_age_lineEdit.text()
        work_exp = self.ui.work_exeperience_lineEdit.text()
        work_ckd = self.ui.work_schedule_lineEdit.text()
        self.ui.officer_name_lineEdit.clear()
        self.ui.officer_second_name_lineEdit.clear()
        self.ui.officer_age_lineEdit.clear()
        self.ui.work_exeperience_lineEdit.clear()
        self.ui.work_schedule_lineEdit.clear()
        self.ui.add_client.setDisabled(True)
        self.ui.clear_officer.setDisabled(True)

    def click_add_wepon(self):
        global mark, calibr, ammo, status
        mark = self.ui.wepon_mark_lineEdit.text()
        calibr = self.ui.wepon_calibr_lineEdit.text()
        ammo = self.ui.wepon_ammo_lineEdit.text()
        if self.ui.action_radioButton1.isChecked():
            status = True
        else:
            status = False
        self.ui.wepon_mark_lineEdit.clear()
        self.ui.wepon_calibr_lineEdit.clear()
        self.ui.wepon_ammo_lineEdit.clear()
        self.ui.action_radioButton1.setDisabled(True)
        self.ui.action_radioButton2.setDisabled(True)
        self.ui.wepon_comboBox.setDisabled(True)
        self.ui.add_wepon.setDisabled(True)
        self.ui.clear_wepon.setDisabled(True)

    def click_add_list_of_upgrades(self):
        global scope, handel, mag, type_of_mag, type_of_bulets
        scope = self.ui.upgrades_scope_lineEdit.text()
        handel = self.ui.upgrades_handle_lineEdit.text()
        mag = self.ui.upgrade_mag_lineEdit.text()
        type_of_mag = self.ui.upgrades_type_of_mag_lineEdit.text()
        type_of_bulets = self.ui.upgrade_type_of_ammo_lineEdit.text()
        self.ui.upgrades_scope_lineEdit.clear()
        self.ui.upgrades_handle_lineEdit.clear()
        self.ui.upgrade_mag_lineEdit.clear()
        self.ui.upgrades_type_of_mag_lineEdit.clear()
        self.ui.upgrade_type_of_ammo_lineEdit.clear()
        self.ui.add_list_of_upgrades.setDisabled(True)
        self.ui.clear_upgrade.setDisabled(True)

    # form changer
    def click_to_officer(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def click_to_wepon(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def click_to_list_upgrades(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    @db_session
    def click_to_list(self):
        client = Client(name_of_client, second_name_of_client, age_of_client, type_of_visit)
        officer = ShootingOfficer(name_of_officer, second_name_of_officer, age_of_officer, work_exp, work_ckd)
        wepon = Wepons(mark, calibr, ammo)
        list_of_upgrades = List_of_upgrades(scope, handel, mag, type_of_mag, type_of_bulets)
        cur_wepon = Cur_wepon(wepon, list_of_upgrades)
        action = Action(status)
        self.ui.stackedWidget.setCurrentIndex(0)

    # fields cleaners
    def click_client_clear(self):
        self.ui.client_name_line_Edit.clear()
        self.ui.client_second_name_line_Edit.clear()
        self.ui.client_age_line_Edit.clear()
        self.ui.type_of_visit_radioButton1.setChecked(False)
        self.ui.type_of_visit_radioButton2.setChecked(False)

    def click_clear_officer(self):
        self.ui.officer_name_lineEdit.clear()
        self.ui.officer_second_name_lineEdit.clear()
        self.ui.officer_age_lineEdit.clear()
        self.ui.work_exeperience_lineEdit.clear()
        self.ui.work_schedule_lineEdit.clear()

    def click_clear_wepon(self):
        self.ui.wepon_mark_lineEdit.clear()
        self.ui.wepon_calibr_lineEdit.clear()
        self.ui.wepon_ammo_lineEdit.clear()
        self.ui.action_radioButton1.setChecked(False)
        self.ui.action_radioButton2.setChecked(False)

    def click_clear_upgrade(self):
        self.ui.upgrades_scope_lineEdit.clear()
        self.ui.upgrades_handle_lineEdit.clear()
        self.ui.upgrade_mag_lineEdit.clear()
        self.ui.upgrades_type_of_mag_lineEdit.clear()
        self.ui.upgrade_type_of_ammo_lineEdit.clear()

    # obj cancel
    # -1073740791 (0xC0000409)
    def click_cancel_client(self):
        self.ui.client_name_line_Edit.setText(name_of_client)
        self.ui.client_second_name_line_Edit.setText(second_name_of_client)
        self.ui.client_age_line_Edit.setText(str(age_of_client))
        if type_of_visit:
            self.ui.type_of_visit_radioButton1.isChecked()
        else:
            self.ui.type_of_visit_radioButton2.isChecked()
        self.ui.add_client.setDisabled(False)
        self.ui.client_clear.setDisabled(False)
        self.ui.type_of_visit_radioButton1.setDisabled(False)
        self.ui.type_of_visit_radioButton2.setDisabled(False)
        self.ui.client_comboBox.setDisabled(False)

    def click_cancel_officer(self):
        self.ui.officer_name_lineEdit.setText(name_of_officer)
        self.ui.officer_second_name_lineEdit.setText(second_name_of_officer)
        self.ui.officer_age_lineEdit.setText(age_of_officer)
        self.ui.work_exeperience_lineEdit.setText(work_exp)
        self.ui.work_schedule_lineEdit.setText(work_ckd)
        self.ui.add_client.setDisabled(False)
        self.ui.clear_officer.setDisabled(False)
        self.ui.officer_comboBox.setDisabled(False)

    def click_cancel_wepon(self):
        self.ui.wepon_mark_lineEdit.setText(mark)
        self.ui.wepon_calibr_lineEdit.setText(calibr)
        self.ui.wepon_ammo_lineEdit.setText(ammo)
        if status:
            self.ui.action_radioButton1.isChecked()
        else:
            self.ui.action_radioButton2.isChecked()
        self.ui.action_radioButton1.setDisabled(False)
        self.ui.action_radioButton2.setDisabled(False)
        self.ui.add_wepon.setDisabled(False)
        self.ui.clear_wepon.setDisabled(False)
        self.ui.wepon_comboBox.setDisabled(False)

    def click_cancel_upgrade(self):
        self.ui.upgrades_scope_lineEdit.setText(scope)
        self.ui.upgrades_handle_lineEdit.setText(handel)
        self.ui.upgrade_mag_lineEdit.setText(mag)
        self.ui.upgrade_type_of_ammo_lineEdit.setText(type_of_bulets)
        self.ui.upgrades_type_of_mag_lineEdit.setText(type_of_mag)
        self.ui.add_list_of_upgrades.setDisabled(False)
        self.ui.clear_upgrade.setDisabled(False)

    def click_back_to_client(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.client_name_line_Edit.setText(name_of_client)
        self.ui.client_second_name_line_Edit.setText(second_name_of_client)
        self.ui.client_age_line_Edit.setText(str(age_of_client))
        if type_of_visit:
            self.ui.type_of_visit_radioButton1.isChecked()
        else:
            self.ui.type_of_visit_radioButton2.isChecked()
        self.ui.add_client.setDisabled(False)
        self.ui.client_clear.setDisabled(False)
        self.ui.type_of_visit_radioButton1.setDisabled(False)
        self.ui.type_of_visit_radioButton2.setDisabled(False)
        self.ui.client_comboBox.setDisabled(False)

    def click_back_to_officer(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.officer_name_lineEdit.setText(name_of_officer)
        self.ui.officer_second_name_lineEdit.setText(second_name_of_officer)
        self.ui.officer_age_lineEdit.setText(age_of_officer)
        self.ui.work_exeperience_lineEdit.setText(work_exp)
        self.ui.work_schedule_lineEdit.setText(work_ckd)
        self.ui.add_client.setDisabled(False)
        self.ui.clear_officer.setDisabled(False)
        self.ui.officer_comboBox.setDisabled(False)

    def click_back_to_wepon(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.ui.wepon_mark_lineEdit.setText(mark)
        self.ui.wepon_calibr_lineEdit.setText(calibr)
        self.ui.wepon_ammo_lineEdit.setText(ammo)
        if status:
            self.ui.action_radioButton1.isChecked()
        else:
            self.ui.action_radioButton2.isChecked()
        self.ui.action_radioButton1.setDisabled(False)
        self.ui.action_radioButton2.setDisabled(False)
        self.ui.add_wepon.setDisabled(False)
        self.ui.clear_wepon.setDisabled(False)
        self.ui.wepon_comboBox.setDisabled(False)




