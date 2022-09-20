import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap

class MainWindow(QWidget):
    def __init__(self):
        """constructor for Empty windows """
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application"""
        # setGeometry()两个参数用于指定窗口显示的位置, 后两个参数用于指定窗口大小
        self.setGeometry(100, 100, 250 , 250)
        self.setWindowTitle("Empty window in PyQt")

        self.setupMainWindow()
        self.show()

    def setupMainWindow(self):
        """Create Qlabel to be displayed in the main windows"""
        hello_label = QLabel(self)
        hello_label.setText(('hello'))
        hello_label.move(105, 15)

        image = '../Beginning-PyQt--second-edition/Chapter02/images/world.png'
        try:
            with open(image):
                world_label = QLabel(self)
                pixmap = QPixmap(image)
                world_label.setPixmap(pixmap)
                world_label.move(25, 40)
        except FileNotFoundError as error:
            print(f"Image not found. \nError: {error}")
# Run the program
app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())
