# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registration.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import images_rc

class Ui_RegWindow(object):
    def setupUi(self, RegWindow):
        if not RegWindow.objectName():
            RegWindow.setObjectName(u"RegWindow")
        RegWindow.resize(1200, 800)
        self.centralwidget = QWidget(RegWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 255)")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(180, 20, 201, 181))
        self.label_6.setStyleSheet(u"image: url(:/logo/images/png/logo-color.png);")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 200, 531, 541))
        self.frame_4.setStyleSheet(u"background-color: rgb(213, 224, 244);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.frame_4)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 511, 312))
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-width: 2px; \n"
"border-style: solid;\n"
"border-color: black;")

        self.horizontalLayout_2.addWidget(self.lineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-width: 2px; \n"
"border-style: solid;\n"
"border-color: black;")

        self.horizontalLayout_3.addWidget(self.lineEdit_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-width: 2px; \n"
"border-style: solid;\n"
"border-color: black;")

        self.horizontalLayout_4.addWidget(self.lineEdit_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_5)

        self.lineEdit_5 = QLineEdit(self.widget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-width: 2px; \n"
"border-style: solid;\n"
"border-color: black;")

        self.horizontalLayout_6.addWidget(self.lineEdit_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.radioButton = QRadioButton(self.widget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setFont(font)

        self.horizontalLayout_7.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.widget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font)

        self.horizontalLayout_7.addWidget(self.radioButton_2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_4)

        self.horizontalSpacer_2 = QSpacerItem(38, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.dateEdit = QDateEdit(self.widget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_8.addWidget(self.dateEdit)

        self.horizontalSpacer = QSpacerItem(48, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u":/logo/images/icons/calendar-lines.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)

        self.horizontalLayout_8.addWidget(self.pushButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.horizontalLayout_12.addWidget(self.label_9)

        self.lineEdit_7 = QLineEdit(self.widget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-width: 2px; \n"
"border-style: solid;\n"
"border-color: black;")

        self.horizontalLayout_12.addWidget(self.lineEdit_7)


        self.verticalLayout_6.addLayout(self.horizontalLayout_12)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.horizontalLayout_9.addWidget(self.label_7)

        self.lineEdit_4 = QLineEdit(self.widget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-width: 2px; \n"
"border-style: solid;\n"
"border-color: black;")
        self.lineEdit_4.setEchoMode(QLineEdit.Password)
        self.lineEdit_4.setClearButtonEnabled(True)

        self.horizontalLayout_9.addWidget(self.lineEdit_4)

        self.password_icon_1 = QLabel(self.widget)
        self.password_icon_1.setObjectName(u"password_icon_1")

        self.horizontalLayout_9.addWidget(self.password_icon_1)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.horizontalLayout_10.addWidget(self.label_8)

        self.lineEdit_6 = QLineEdit(self.widget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-width: 2px; \n"
"border-style: solid;\n"
"border-color: black;")
        self.lineEdit_6.setEchoMode(QLineEdit.Password)
        self.lineEdit_6.setDragEnabled(False)
        self.lineEdit_6.setClearButtonEnabled(True)

        self.horizontalLayout_10.addWidget(self.lineEdit_6)

        self.confirm_icon = QLabel(self.widget)
        self.confirm_icon.setObjectName(u"confirm_icon")

        self.horizontalLayout_10.addWidget(self.confirm_icon)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(430, 0, 151, 31))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.frame_5)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon1 = QIcon()
        icon1.addFile(u":/logo/images/icons/minus-small.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)

        self.horizontalLayout_11.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_5)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon2 = QIcon()
        icon2.addFile(u":/logo/images/icons/arrow-up-right-and-arrow-down-left-from-center.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)

        self.horizontalLayout_11.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_5)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon3 = QIcon()
        icon3.addFile(u":/logo/images/icons/cross.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon3)

        self.horizontalLayout_11.addWidget(self.pushButton_4)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(12, 393, 561, 373))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_2)

        RegWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(RegWindow)

        QMetaObject.connectSlotsByName(RegWindow)
    # setupUi

    def retranslateUi(self, RegWindow):
        RegWindow.setWindowTitle(QCoreApplication.translate("RegWindow", u"MainWindow", None))
        self.label_6.setText("")
        self.label.setText(QCoreApplication.translate("RegWindow", u"\u0423\u0440\u0433\u0438\u0439\u043d \u043e\u0432\u043e\u0433:              ", None))
        self.label_2.setText(QCoreApplication.translate("RegWindow", u"\u041e\u0432\u043e\u0433:                           ", None))
        self.label_3.setText(QCoreApplication.translate("RegWindow", u"\u041d\u044d\u0440:                             ", None))
        self.label_5.setText(QCoreApplication.translate("RegWindow", u"\u04ae\u043d\u0434\u044d\u0441 \u0443\u0433\u0441\u0430\u0430:              ", None))
        self.radioButton.setText(QCoreApplication.translate("RegWindow", u"\u042d\u0440\u044d\u0433\u0442\u044d\u0439", None))
        self.radioButton_2.setText(QCoreApplication.translate("RegWindow", u"\u042d\u043c\u044d\u0433\u0442\u044d\u0439", None))
        self.label_4.setText(QCoreApplication.translate("RegWindow", u"\u0422\u04e9\u0440\u0441\u04e9\u043d \u043e\u0433\u043d\u043e\u043e:", None))
        self.pushButton.setText("")
        self.label_9.setText(QCoreApplication.translate("RegWindow", u"\u041d\u044d\u0432\u0442\u0440\u044d\u0445 \u043d\u044d\u0440:              ", None))
        self.label_7.setText(QCoreApplication.translate("RegWindow", u"\u041d\u0443\u0443\u0446 \u04af\u0433:                        ", None))
        self.password_icon_1.setText("")
        self.label_8.setText(QCoreApplication.translate("RegWindow", u"\u041d\u0443\u0443\u0446 \u04af\u0433\u044d\u044d \u0434\u0430\u0432\u0442\u0430\u043d\u0430 \u0443\u0443", None))
        self.confirm_icon.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
    # retranslateUi

