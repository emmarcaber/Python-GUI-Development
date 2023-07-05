from PySide6 import QtWidgets, QtCore
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()

class UserInterface(QtCore.QObject):

    def __init__(self):
        self.ui = loader.load('widget.ui', None)
        self.ui.setWindowTitle("User Data")
        self.ui.submit_button.clicked.connect(self.do_something)
        self.ui.occupation_line_edit.returnPressed.connect(self.do_something)
        self.ui.full_name_line_edit.returnPressed.connect(self.do_something)

    def do_something(self):
            print(f"{self.ui.full_name_line_edit.text()} is a {self.ui.occupation_line_edit.text()}")

    def show(self):
        self.ui.show()