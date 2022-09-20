import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap, QFont

class MainWindow(QWidget):
    def __init__(self):
        """constructor for Empty windows """
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application"""
        # setGeometry()两个参数用于指定窗口显示的位置, 后两个参数用于指定窗口大小
        self.setGeometry(500, 500, 250, 400)
        self.setWindowTitle("User profile")

        self.setupMainWindow()
        self.show()
    def creatImageLabels(self):
        """Create Qlabel to be displayed in the main windows"""
        skyblue_path = '../Beginning-PyQt-resource/Chapter02/images/skyblue.png'
        try:
            with open(skyblue_path):
                skyblue = QLabel(self)
                pixmap = QPixmap(skyblue_path)
                skyblue.setPixmap(pixmap)
        except FileNotFoundError as error:
            print(f"Image not found. \nError: {error}")
        profile_path = '../Beginning-PyQt-resource/Chapter02/images/profile_image.png'
        try:
            with open(profile_path):
                profile = QLabel(self)
                pixmap = QPixmap(profile_path)
                profile.setPixmap(pixmap)
                profile.move(80, 20)
        except FileNotFoundError as error:
            print(f"Image not found. \nError: {error}")

    def setupMainWindow(self):
        self.creatImageLabels()

        user_label = QLabel(self)
        user_label.setText("John Doe")
        user_label.setFont(QFont("Arial", 20))
        user_label.move(85, 140)

        bio_label = QLabel(self)
        bio_label.setText("Biography")
        bio_label.setFont(QFont("Arial", 17))
        bio_label.move(15, 170)

        about_label = QLabel(self)
        about_label.setText("I'm a software Engineer with 10 years\
                            exprience creating awesome code!")
        about_label.setWordWrap(True)   # set auto line
        about_label.move(15, 190)
# Run the program
app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())
