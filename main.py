from PyQt6.QtWidgets import QApplication,QMainWindow, QTableWidget
from PyQt6.QtGui import QAction
import sys

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("StudentManagementSystem")

        # create Menu Bar
        file_menu = self.menuBar().addMenu("&File")
        help_menu = self.menuBar().addMenu("&Help")

        add_student = QAction('Add Student',self)
        file_menu.addAction(add_student)

        about = QAction('About', self)
        help_menu.addAction(about)

        # Creating a table structure
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(('Id','Name','Course','Mobile'))

        self.setCentralWidget(self.table)


app = QApplication(sys.argv)
sms = MainWindow()
sms.show()
sys.exit(app.exec())