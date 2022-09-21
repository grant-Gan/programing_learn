# message_boxes.py
# Import necessary modules

"""
There are two kinds of dialog boxes. Modal dialogs block user interaction from the
rest of the program until the dialog box is closed. Modeless dialogs allow the user to
interact with both the dialog and the rest of the application.
"""

import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel,
    QMessageBox, QLineEdit, QPushButton)
from PyQt6.QtGui import QFont
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setFixedSize(340, 160)
        self.setWindowTitle("QMessageBox Example")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        Catalogue_label = QLabel('Author Catalogue', self)
        Catalogue_label.move(80, 20)
        Catalogue_label.setFont(QFont('Arial', 16))

        search = QLabel('Search the index for an author: ',self)
        search.move(20, 50)
        search.setFont(QFont('Arial', 11))

        name = QLabel('Name: ', self)
        name.move(20, 80)
        name.setFont(QFont('Arial', 11))

        self.search_lineEdit = QLineEdit(self)
        self.search_lineEdit.move(70, 80)
        self.search_lineEdit.resize(230, 20)
        # lineEdit.setPlaceholderText()用于设置提示性的输入框中提示性的文字.
        self.search_lineEdit.setPlaceholderText('Enter name as: Frist Last')
        # setText()直接填充了文字
        # self.search_lineEdit.setText('Enter name as: Frist Last')

        search_button = QPushButton('Search', self)
        search_button.move(130, 120)
        search_button.clicked.connect(self.searchAuthors)

    def searchAuthors(self):
        file = 'files/author.txt'

        try:
            with open(file, 'r') as f:
                authors = [line.rstrip('\n') for line in f]

            if self.search_lineEdit.text() in authors:
                QMessageBox.information(self, 'Author Found',
                                        'Author found in catalogue!',
                                        QMessageBox.StandardButton.Ok)
            else :
                answer = QMessageBox.question(self,
                                              'Author Not Found',
                                              """
                                              <p>Author not fond in catalogue.</p>
                                              <p>Do you wish yo continue?</p>
                                              """,
                                              QMessageBox.StandardButton.Yes| \
                                              QMessageBox.StandardButton.No,
                                              QMessageBox.StandardButton.No)
                                              # 这里的最后一个参数用于指定默认和高亮的按钮
                if answer == QMessageBox.StandardButton.No:
                    print('Closing application.')
                    self.close()

        except FileNotFoundError as error:
            QMessageBox.warning(self,
                                'Error',
                                f"""
                                <p>File not found.</p>
                                <hr>
                                <p>Error: {error}</p>
                                <p>Closing application</p>
                                """,
                                QMessageBox.StandardButton.Ok)
            self.close()


app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())