import sys
from PyQt6.QtWidgets import (QWidget, QCheckBox, QLabel, QLineEdit,
                             QPushButton, QApplication, QMessageBox, QDialog)
from PyQt6.QtGui import QPixmap, QFont

class NewUserDialog(QDialog):

    def __init__(self):
        super(NewUserDialog, self).__init__()
        # setModel 设置模态对话框, 即有该对话时不能与其它窗口交互
        self.setModal(True)
        self.initializeUI()

    def initializeUI(self):
        self.setFixedSize(360, 320)
        self.setWindowTitle('3.1-Registration GUI')
        self.setupWindows()

    def setupWindows(self):
        """Create and arrange widgets in the windows for
        collectiing new account information"""
        login_label = QLabel('Create New Account', self)
        login_label.setFont(QFont('Arial', 20))
        login_label.move(90, 20)

        # Create Qlabel for image
        user_image = '../beginning_resource/Chapter03/images/new_user_icon.png'
        try:
            with open(user_image):
                user_label = QLabel(self)
                pixmap = QPixmap(user_image)
                user_label.setPixmap(pixmap)
                user_label.move(150, 60)
        except FileNotFoundError as error:
            print(f"Image not found, Error: {error}")

        # Create name Qlabel and QlineEdit widgets
        name_label = QLabel('Usrname:', self)
        name_label.move(20, 144)

        self.name_edit = QLineEdit(self)
        self.name_edit.resize(250, 24)
        self.name_edit.move(90, 140)

        # Create password Qlabel and QLineEdit widgets
        new_pwd_lanel = QLabel('Password:', self)
        new_pwd_lanel.move(20, 204)
        self.new_pwd_edit = QLineEdit(self)
        self.new_pwd_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.new_pwd_edit.resize(250, 24)
        self.new_pwd_edit.move(90, 200)

        confiem_label = QLabel('Confirm:', self)
        confiem_label.move(20, 234)

        self.confirm_edit = QLineEdit(self)
        self.confirm_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirm_edit.resize(250, 24)
        self.confirm_edit.move(90, 230)

        sign_up_button = QPushButton('Sign Up', self)
        sign_up_button.resize(320, 32)
        sign_up_button.move(20, 270)
        sign_up_button.clicked.connect(self.confirmSignUp)

    def confirmSignUp(self):
        username_text = self.name_edit.text()
        pwd_text = self.new_pwd_edit.text()
        confirm_text = self.confirm_edit.text()

        if username_text == '' or pwd_text == '':
            # Display QMessageBox id password don't mach
            QMessageBox.warning(
                self,
                'Error Meaage',
                'Please enter username and password value',
                QMessageBox.StandardButton.Close,
                QMessageBox.StandardButton.Close

            )
        elif pwd_text != confirm_text:
            QMessageBox.warning(
                self,
                'Error Message',
                'The password you entered do not match',
                QMessageBox.StandardButton.Close,
                QMessageBox.StandardButton.Close
            )
        else:
            with open('files/users.txt', 'a+') as f:
                f.write('\n' + username_text + ',')
                f.write(pwd_text)
            self.close()











