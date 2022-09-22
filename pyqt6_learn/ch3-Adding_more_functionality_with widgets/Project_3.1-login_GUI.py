import sys
from PyQt6.QtWidgets import (QWidget, QCheckBox, QLabel, QLineEdit,
                             QPushButton, QApplication, QMessageBox)
from PyQt6.QtGui import QPixmap, QFont


class UserWindows(QWidget):
    def __init__(self):
        super(UserWindows, self).__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(500, 500, 600, 800)
        self.setWindowTitle('User windows')
        self.setupUserWindows()

        self.show()

    def setupUserWindows(self):
        try:
            with open('../beginning_resource/Chapter03/images/background_kingfisher.jpg') as f:
                background = QPixmap(f, self)
                bgImg_label = QLabel(background, self)
                bgImg_label.show()

        except FileNotFoundError as erro:
            QMessageBox.warning(
                self,
                'File not found',
                f"""
                <p>Error: {erro}</p>
                """,
                QMessageBox.StandardButton.Ok
            )


class MainWindows(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(500, 500, 340, 250)
        self.setWindowTitle("3.1-Login GUI")
        self.setupMainWindows()

        self.show()

    def setupMainWindows(self):

        self.login_is_successful = False

        login_label = QLabel('Login', self)
        login_label.move(145, 10)
        login_label.setFont(QFont('Arial', 13))

        username_label = QLabel('Username: ', self)
        username_label.move(20, 45)
        self.username_linEdit = QLineEdit(self)
        # username_linEdit.setPlaceholderText('Username')
        self.username_linEdit.setText('admin')
        self.username_linEdit.move(80, 45)
        self.username_linEdit.resize(240, 18)

        username_label = QLabel('Password: ', self)
        username_label.move(20, 70)
        self.pwd_linEdit = QLineEdit(self)
        self.pwd_linEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.pwd_linEdit.move(80, 70)
        self.pwd_linEdit.resize(240, 18)

        self.showpd_checkBox = QCheckBox('Show Password', self)
        self.showpd_checkBox.move(80, 90)
        self.showpd_checkBox.toggled.connect(self.displayPasswordIfChecked)

        self.login_Button = QPushButton('Login', self)
        self.login_Button.setFont(QFont('Aral', 10))
        self.login_Button.resize(300, 25)
        self.login_Button.move(20, 120)
        self.login_Button.clicked.connect(self.clickedLogiButton)

        tip = QLabel('Not a member?', self)
        tip.move(20, 162)
        self.signup_button = QPushButton('Sign Up', self)
        self.signup_button.setFont(QFont('Arial', 8))
        self.signup_button.move(110, 160)
        self.signup_button.resize(70, 20)
        self.signup_button.clicked.connect(self.createNewUser)

    def closeEvent(self, event):
        """
        这个函数应该是QWigth类中的事件,当用户点击关闭窗口时
        这个函数就会被自动调用.
        """

        # 如果此时用户已经登录成功了, 事件就被自动接受.
        if self.login_is_successful == True:
            event.accept()
            pass
        else:
            answer = QMessageBox.question(
                self,
                'Quit application?',
                "Are you sure you want to QUIT?",
                QMessageBox.StandardButton.No | \
                QMessageBox.StandardButton.Yes,
                QMessageBox.StandardButton.No
            )
            if answer == QMessageBox.StandardButton.Yes:
                event.accept()
            elif answer == QMessageBox.StandardButton.No:
                event.ignore()

    def createNewUser(self):
        """Open a dialog for creating a new user"""
        self.create_new_user_windows = NewUserDialog()
        self.create_new_user_windows.show()

    def openApplicationWindows(self):
        """open a application winddows after user login in"""
        self.application_windows = ApplicationWindows()
        self.application_windows.show()

    def displayPasswordIfChecked(self, checked):
        # EchoMode.Normal : 标准模式, 默认
        # Echo.Password : 密码模式, 会隐藏输入的密码
        # Echo.NoEcho: 不显示输入
        # Echo.PasswordEchoOnEdit: 输入时显示, 输完后隐藏
        if checked:
            self.pwd_linEdit.setEchoMode(
                QLineEdit.EchoMode.Normal
            )
        else:
            self.pwd_linEdit.setEchoMode(
                QLineEdit.EchoMode.Password
            )

    def clickedLogiButton(self):
        try:
            users = {}  # Dictionary to store user information
            file_path = 'files/users.txt'
            with open(file_path, 'r') as f:
                for line in f:
                    user_info = line.split(',')
                    username_info = user_info[0]
                    password_info = user_info[1].strip('\n')
                    users[username_info] = password_info

            username = self.username_linEdit.text()
            password = self.pwd_linEdit.text()

            # 这里的items方法会返回(username, password)
            if (username, password) in users.items():
                QMessageBox.information(
                    self,
                    'Login successful',
                    'Login successful',
                    QMessageBox.StandardButton.Ok,
                    QMessageBox.StandardButton.Ok
                )
                self.login_is_successful = True
                self.close()  # close login windows
                self.openApplicationWindows()

            else:
                QMessageBox.warning(
                    self,
                    'Error Message',
                    'The username or password is incorrect.',
                    QMessageBox.StandardButton.Close,
                    QMessageBox.StandardButton.Close
                )

        except FileNotFoundError as error:
            QMessageBox.warning(
                self,
                'Error',
                f"""
                <p>File not found</p>
                <p>Error: {error}</p>
                """,
                QMessageBox.StandardButton.Ok
            )
            # Create file id it doesn't exist
            open(file_path, 'w')


class ApplicationWindows(QWidget):
    def __init__(self):
        super(ApplicationWindows, self).__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setMinimumSize(640, 426)
        self.setWindowTitle('Application')
        self.setupApplicationWindows()

    def setupApplicationWindows(self):
        image_path = '../beginning_resource/Chapter03/images/background_kingfisher.jpg'
        try:
            with open(image_path, 'r') :
                main_label = QLabel(self)
                pixmap = QPixmap(image_path)
                main_label.setPixmap(pixmap)
                main_label.move(0, 0)
        except FileNotFoundError as error:
            print(f"Image not found.\nError: {error}")



class NewUserDialog(QWidget):
    def __init__(self):
        super(NewUserDialog, self).__init__()
        self.setupNewUserDialogUI()


app = QApplication(sys.argv)
windows = MainWindows()
sys.exit(app.exec())
