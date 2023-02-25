# -*- coding: utf-8 -*-
from PyQt6 import QtWidgets, QtGui
from login import Ui_Login
from PyQt6.QtCore import Qt
import sys
from registr import Ui_RegWindow
from calendar import Ui_Calendar
from enum import Enum
from dataclasses import dataclass
from typing import Any
from pathlib import Path



class Sex(Enum):
    MALE = "Эрэгтэй"
    FEMALE = "Эмэгтэй"


class UserRelationshipStatus(Enum):
    MARRIED = "Гэрлэсэн"
    SINGLE = "Гэрлээгүй"


class UserMilitaryDutyStatus(Enum):
    SERVED = "Хаасан"
    UNSERVED = "Хаагаагүй"


@dataclass
class User:
    family_name: str
    surname: str
    given_name: str
    nationality: str
    sex: Sex
    date_of_birth: Any
    username: str
    password: str
    place_of_birth: str
    place_of_birth2: str
    marital_status: UserRelationshipStatus
    military_status: UserMilitaryDutyStatus
    education_status: str
    image: Any
    office: str
    unit: str
    specialization: str
    rank: str
    telephone: str
    email: str
    experience: str
    responsibility: str


class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Login window
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.login)
        self.ui.pushButton_2.clicked.connect(self.register)


        # Registration window
        self.reg = Ui_RegWindow()



    def login(self):
        name = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        print(f"Нэр:{name}, нууц үг {password}")

    def register(self):
        # Showing a registration window
        self.reg.setupUi(self)

        self.family_name = self.reg.lineEdit.text()
        self.surname = self.reg.lineEdit_2.text()
        self.given_name = self.reg.lineEdit_3.text()
        self.nationality = self.reg.lineEdit_5.text()
        self.sex = self.sex_picker()
        self.date_of_birth = self.reg.dateEdit.date().toPyDate()
        self.username = self.reg.lineEdit_7.text()
        self.password = self.reg.lineEdit_4.text()
        self.password_confirmation = self.reg.lineEdit_6.text()
        self.place_of_birth = self.reg.lineEdit_8.text()
        self.place_of_birth2 = self.reg.lineEdit_9.text()
        self.marital_status = self.marital_picker()
        self.military_status = self.military_status_picker()
        self.education_status = self.reg.comboBox.currentText()
        self.image = None
        # self.office =
        # self.unit =
        # self.specialization =
        # self.rank =
        # self.telephone =
        # self.email = 
        # self.experience =
        # self.responsibility =


        # datepick button connecting a function pick_date
        self.reg.pushButton.clicked.connect(self.pick_date)

        self.reg.pushButton_5.clicked.connect(self.image_file_dialog_open)




    def pick_date(self):
        self.calendar_widget = QtWidgets.QMainWindow()
        #calendar window
        self.calendar_form = Ui_Calendar()
        self.calendar_form.setupUi(self.calendar_widget)
        self.calendar_form.calendarWidget.selectionChanged.connect(self.date_select)
        self.calendar_form.pushButton.clicked.connect(self.date_changer)
        self.calendar_form.pushButton_2.clicked.connect(self.calendar_cancel)
        self.calendar_widget.show()

    def date_select(self):
        self.date_selected = self.calendar_form.calendarWidget.selectedDate()
        self.calendar_form.label.setText(str(self.date_selected.toPyDate()))
        # print(self.date_selected)

    def date_changer(self):
        self.reg.dateEdit.setDate(self.date_selected)
        self.calendar_widget.close()


    def calendar_cancel(self):
        self.calendar_widget.close()

    def sex_picker(self) -> Sex | None:
        if self.reg.radioButton.isChecked():
            return Sex.MALE
        elif self.reg.radioButton_2.isChecked():
            return Sex.FEMALE
        else:
            return None

    def marital_picker(self) -> UserRelationshipStatus | None:
        if self.reg.radioButton_3.isChecked():
            return UserRelationshipStatus.MARRIED
        elif self.reg.radioButton_4.isChecked():
            return UserRelationshipStatus.SINGLE
        else:
            return None

    def military_status_picker(self) -> UserRelationshipStatus | None:
        if self.reg.radioButton_5.isChecked():
            return UserMilitaryDutyStatus.SERVED
        elif self.reg.radioButton_6.isChecked():
            return UserMilitaryDutyStatus.UNSERVED
        else:
            return None

    def image_file_dialog_open(self):
        self.filename = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", Path.cwd().name, 
                                                         "All Files (*);;PNG Files (*.png);;JPG Files (*.jpg)")
        self.pixmap = QtGui.QPixmap(self.filename[0])
        self.reg.label_16.setPixmap(self.pixmap)
        self.reg.label_16.setScaledContents(True)
        print(type(self.pixmap))
        self.image = self.pixmap
        return self.image





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())

