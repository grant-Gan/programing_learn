import sys
from PyQt6.QtWidgets import (QWidget, QLabel, QCheckBox, QPushButton,
                             QApplication, QVBoxLayout, QButtonGroup)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class MainWindows(QWidget):
    def __init__(self):
        super(MainWindows, self).__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setFixedWidth(600)
        self.setMinimumHeight(400)
        self.setWindowTitle('QVBoxLayout Example')
        self.setupWindows()
        self.show()

    def setupWindows(self):
        one_check_box = QCheckBox('Satisdied')
        two_check_box = QCheckBox('Average')
        header_label = QLabel('Chez PyQt6')
        header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        v_box = QVBoxLayout()
        v_box.addWidget(one_check_box)
        v_box.addWidget(two_check_box)
        v_box.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.setLayout(v_box)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = MainWindows()
    sys.exit(app.exec())