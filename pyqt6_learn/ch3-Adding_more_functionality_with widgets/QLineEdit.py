import os
import sys

from PyQt6.QtWidgets import (QWidget, QApplication, QLabel, QLineEdit, QPushButton)
from PyQt6.QtCore import Qt

class MainWindows(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setMaximumSize(310, 130)
        self.setWindowTitle('QLineEdit Example')

        self.setMainWindows()
        self.show()

    def setMainWindows(self):
        QLabel('Please enter you name below.',self).move(70, 10)
        name_label = QLabel('Name:', self)
        name_label.move(20, 50)

        self.name_edit = QLineEdit(self)
        self.name_edit.resize(201, 20)
        self.name_edit.move(70, 50)

        clear_button = QPushButton('Clear', self)
        clear_button.move(140, 90)
        clear_button.clicked.connect(self.clearText)

        accept_button = QPushButton('OK', self)
        accept_button.move(210, 90)
        accept_button.clicked.connect(self.acceptText)

    def clearText(self):
        # self.name_edit.clear()
        self.name_edit.text()

    def acceptText(self):
        accept = self.name_edit.text()
        print(accept)

app = QApplication(sys.argv)
windows = MainWindows()
sys.exit(app.exec())