import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class PasswordConfirmation(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Password Confirmation')

        self.password_label = QLabel('Password:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.confirm_label = QLabel('Confirm Password:')
        self.confirm_input = QLineEdit()
        self.confirm_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.submit_passwords)

        vbox = QVBoxLayout()
        vbox.addWidget(self.password_label)
        vbox.addWidget(self.password_input)
        vbox.addWidget(self.confirm_label)
        vbox.addWidget(self.confirm_input)
        vbox.addWidget(self.submit_button)

        self.setLayout(vbox)

    def submit_passwords(self):
        if self.password_input.text() == self.confirm_input.text():
            self.accept()
        else:
            self.password_input.setText('')
            self.confirm_input.setText('')
            self.password_input.setFocus()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    password_confirmation = PasswordConfirmation()
    while not password_confirmation.exec():
        pass
    sys.exit(app.exec())

