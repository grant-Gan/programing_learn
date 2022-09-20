import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap

class EmpeyWindos(QWidget):
    def __init__(self):
        """constructor for Empty windows """
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application"""
        # setGeometry()两个参数用于指定窗口显示的位置, 后两个参数用于指定窗口大小
        self.setGeometry(100, 100, 250 , 250)
        self.setWindowTitle("Empty window in PyQt")
        self.show()

# Run the program
app = QApplication(sys.argv)
window = EmpeyWindos()
sys.exit(app.exec())
