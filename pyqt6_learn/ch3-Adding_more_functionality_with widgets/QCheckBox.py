import os
import sys

from PyQt6.QtWidgets import (QWidget, QLabel, QCheckBox, QApplication)
from PyQt6.QtCore import Qt

class MainWindows(QWidget):
    def __init__(self):
        super(MainWindows, self).__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setFixedSize(250, 150)
        self.setWindowTitle('QCheckBox Exampple')

        self.setUpMainWindows()
        self.show()

    def setUpMainWindows(self):
        header_label = QLabel('Which shifts can you work?'
                              '(Please check all that apply)', self)
        header_label.setWordWrap(True)
        header_label.move(20, 10)

        # set up the checkBoxs
        morning_cb = QCheckBox('Morning [8 AM - 2 PM]', self)
        morning_cb.move(40, 60)
        # toggle 方法用于设定该选择框默认被选中.
        morning_cb.toggle()   # Uncomment to start checked
        morning_cb.toggled.connect(self.printSelected)

        after_cb = QCheckBox('Afternoon [1 PM - 8 PM]', self)
        after_cb.move(40, 80)
        after_cb.toggled.connect(self.printSelected)

        night_cb = QCheckBox('Night [7 PM - 3 AM]', self)
        night_cb.move(40, 100)
        night_cb.toggled.connect(self.printSelected)

    def printSelected(self, checked):
        """
        toogled 信号好会传递额外的信息: checked, 这个信号用于表示复选框是否被选中
        如果被选中, 返回True否则就返回False.
        sender()可以用来判断是哪一个widgwt发送的信号.
        """
        sender = self.sender()
        if checked:
            print(f"{sender.text()} selected")
        else:
            print(f"{sender.text()} Deselected.")


app = QApplication(sys.argv)
windows = MainWindows()
sys.exit(app.exec())