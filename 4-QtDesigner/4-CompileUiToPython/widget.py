"""
NOTE:
    You can generate the ready-made python file of the .ui file. By using the commmand:

    ```
        pyside6-uic [filename.ui] > [ui_filename.py]
    ```

    If you encounter an error of "Python Source Code String Cannot Contain Null Bytes".
    You can check the encoding on the right bottom side of VSCode. Then, just click on the encoding 
    and select "Save with Encoding" and select UTF-8.
"""

from PySide6.QtWidgets import QWidget
from ui_widget import Ui_Widget

class Widget(QWidget, Ui_Widget):

    def __init__(self):
        super().__init__()

        # NOTE: Always setup the UI first to modify it
        self.setupUi(self)
        self.setWindowTitle("User Data")

        self.submit_button.clicked.connect(self.do_something)

        # You can press enter in any textbox or QLineEdit, 
        # then the form will be submitted
        self.full_name_line_edit.returnPressed.connect(self.do_something)
        self.section_line_edit.returnPressed.connect(self.do_something)

    # Submit Button Slot
    def do_something(self):
        print(f"{self.full_name_line_edit.text()} - {self.section_line_edit.text()}")