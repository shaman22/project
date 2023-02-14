# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import images_rc

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(795, 762)
        Login.setMinimumSize(QSize(795, 762))
        Login.setMaximumSize(QSize(795, 16777215))
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 771, 741))
        self.frame.setStyleSheet(u"background-color: #235F75;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 771, 581))
        self.widget.setStyleSheet(u"background-color: #235F75;")
        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 771, 441))
        self.frame_2.setStyleSheet(u"background-image: url(:/images/images/large.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-size: auto;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(160, 440, 451, 141))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.vboxLayout = QVBoxLayout(self.frame_3)
        self.vboxLayout.setSpacing(0)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.frame_3)
        self.lineEdit.setObjectName(u"lineEdit")
        font = QFont()
        font.setFamily(u"Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"background-color: #FFDE59;")
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.vboxLayout.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.frame_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(u"background-color: #FFDE59;")
        self.lineEdit_2.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setAlignment(Qt.AlignCenter)

        self.vboxLayout.addWidget(self.lineEdit_2)

        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(160, 580, 451, 111))
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"background-color: #FFDE59;")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"background-color: #FFDE59;")

        self.horizontalLayout.addWidget(self.pushButton_2)

        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"MainWindow", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Login", u"\u041d\u044d\u0432\u0442\u0440\u044d\u0445 \u043d\u044d\u0440", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Login", u"\u041d\u0443\u0443\u0446 \u04af\u0433", None))
        self.pushButton.setText(QCoreApplication.translate("Login", u"\u041d\u044d\u0432\u0442\u0440\u044d\u0445", None))
        self.pushButton_2.setText(QCoreApplication.translate("Login", u"\u0411\u04af\u0440\u0442\u0433\u04af\u04af\u043b\u044d\u0445", None))
    # retranslateUi

