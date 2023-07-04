import sys

from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()                        # Set up a loader object

app = QtWidgets.QApplication(sys.argv)
window = loader.load('widget.ui', None)     # Load the UI - happens at run time!

def do_something():
    print(f"{window.full_name_line_edit.text()} is a {window.occupation_line_edit.text()}")

# Access the widgets in the form
window.submit_button.clicked.connect(do_something)

# Changes the properties of the window
window.setWindowTitle("User Data")
window.show()

app.exec()