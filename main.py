from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QDialog, QVBoxLayout,\
    QLineEdit, QComboBox, QPushButton
from PyQt6.QtGui import QAction
import sys
import sqlite3


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.resize(500, 300)
        self.setWindowTitle("StudentManagementSystem")

        # create Menu Bar
        file_menu = self.menuBar().addMenu("&File")
        help_menu = self.menuBar().addMenu("&Help")
        search_menu = self.menuBar().addMenu("&Edit")

        add_student = QAction('Add Student', self)
        add_student.triggered.connect(self.adding_student)
        file_menu.addAction(add_student)

        about = QAction('About', self)
        help_menu.addAction(about)

        filter = QAction('search', self)
        filter.triggered.connect(self.search_record)
        search_menu.addAction(filter)

        # Creating a table structure
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(('Id', 'Name', 'Course', 'Mobile'))
        # To remove/hide extra index by default
        self.table.verticalHeader().setVisible(False)

        self.setCentralWidget(self.table)

    def load_data(self):
        connection = sqlite3.connect('database.db')
        all_data = list(connection.execute("select * from students"))
        # Set rows with None before arranging
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(all_data):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()

    def adding_student(self):
        dialog = InsertDialog()
        dialog.exec()

    def search_record(self):
        dialog = SearchDialog()
        dialog.exec()

class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("StudentManagementSystem")
        # Good Practise for Dialog Window
        self.setFixedWidth(300)
        self.setFixedHeight(300)
        layout = QVBoxLayout()

        # Create widgets
        self.sname = QLineEdit()
        self.sname.setPlaceholderText("Name")
        layout.addWidget(self.sname)

        self.coursecombo = QComboBox()
        self.coursecombo.addItems(['Biology','Maths','Physics','Telugu'])
        layout.addWidget(self.coursecombo)

        self.mobile = QLineEdit()
        self.mobile.setPlaceholderText("Mobile")
        layout.addWidget(self.mobile)

        button = QPushButton("submit")
        button.clicked.connect(self.insert_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def insert_student(self):
        name = self.sname.text()
        course = self.coursecombo.currentText()
        mobile = self.mobile.text()

        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("Insert into students(name,course,mobile) values (?,?,?)", (name, course, mobile))
        connection.commit()
        self.sname.setText("")
        self.mobile.setText("")
        cursor.close()
        connection.close()
        sms.load_data()

class SearchDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search Student")
        self.setFixedWidth(300)
        self.setFixedHeight(300)
        layout = QVBoxLayout()

        self.searchbar = QLineEdit()
        self.searchbar.setPlaceholderText("Name")
        layout.addWidget(self.searchbar)

        searchbutton = QPushButton("Search")
        searchbutton.clicked.connect(self.filter_data)
        layout.addWidget(searchbutton)

        self.setLayout(layout)
    def filter_data(self):
        pass

app = QApplication(sys.argv)
sms = MainWindow()
sms.load_data()
sms.show()
sys.exit(app.exec())
