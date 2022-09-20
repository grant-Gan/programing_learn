import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton)
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 250, 150)
        self.setWindowTitle("QPushButton Example")

        self.setupMainWindow()
        self.show()

    def setupMainWindow(self):
        self.time_pressed = 0

        self.name_label = QLabel("Don't push the button.", self)
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.name_label.move(60, 30)

        self.button = QPushButton("Push Me", self)
        self.button.move(80, 70)
        self.button.clicked.connect(self.buttonCliked)

    def buttonCliked(self):
        self.time_pressed += 1

        if self.time_pressed == 1:
            self.name_label.setText("Why'd you press me?")
        elif self.time_pressed == 2:
            self.name_label.setText("I'm warning you.")
            self.button.setText(("你再试试?"))
            self.button.adjustSize()
            self.button.move(80, 90)
        elif self.time_pressed == 3:
            print("The window has been closed.")
            self.close()

app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())