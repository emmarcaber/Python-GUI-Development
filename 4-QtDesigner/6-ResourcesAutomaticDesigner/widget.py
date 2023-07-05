"""
NOTE:
    You can generate the ready-made python file of .qrc file. By using the command:

    ```
        pyside6-rcc [filename.qrc] -o [filename-rc.py]
    ```
"""

from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon
from ui_widget import Ui_Form

import resource_rc              # Manually import the compiled resource file

class Widget(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("User Data")

        self.spin_box.setValue(50)

        self.plus_button.clicked.connect(self.plus)
        self.minus_button.clicked.connect(self.minus)

    def plus(self):
        value = self.spin_box.value()
        self.spin_box.setValue(value + 1)

    def minus(self):
        value = self.spin_box.value()
        self.spin_box.setValue(value - 1)

