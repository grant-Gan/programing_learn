import sys
from PyQt6.QtWidgets import (QWidget, QApplication, QLabel, QLineEdit, 
                             QPushButton, QHBoxLayout)

class MainWindows(QWidget):
    def __init__(self):
        super(MainWindows, self).__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setMinimumWidth(500)
        self.setFixedHeight(60)
        self.setWindowTitle('QHBoxLayout Example')

        self.setupWindows()
        self.show()

    def setupWindows(self):

        # 初始化QWidgets对象的时候不再需要传递self参数, 因为层管理其会自动传入
        name_label = QLabel('New Username:')

        name_edit = QLineEdit()
        name_edit.setClearButtonEnabled(True)   # 设置清空按钮
        name_edit.textEdited.connect(self.checkUserInput)

        self.accept_button = QPushButton('Confirm')
        self.accept_button.setEnabled(False)    # 设置按钮不可用
        self.accept_button.clicked.connect(self.close)

        main_h_box = QHBoxLayout()
        main_h_box.addWidget(name_label)
        main_h_box.addWidget(name_edit)
        main_h_box.addWidget(self.accept_button)
        self.setLayout(main_h_box)

    def checkUserInput(self, text):
        if len(text) > 0 \
            and all(t.isalpha() or t.isdigit() for t in text):
            self.accept_button.setEnabled(True)
        else:
            self.accept_button.setEnabled(False)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    windwos = MainWindows()
    sys.exit(app.exec())