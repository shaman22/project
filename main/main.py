# -*- coding: utf-8 -*-
from PySide2 import QtWidgets, QtGui
from login import Ui_Login
from PySide2.QtCore import Qt
import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.login)
        self.ui.pushButton_2.clicked.connect(self.register)

    def login(self):
        name = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        print(f"Нэр:{name}, нууц уг {password}")

    def register(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
        
