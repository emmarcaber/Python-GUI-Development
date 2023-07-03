from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class Widget(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLabel Images Demo")

        label = QLabel()
        label.setPixmap(QPixmap("images/minions.png"))      # Pass the relative path of the image you want to insert

        layout = QVBoxLayout()
        layout.addWidget(label)

        self.setLayout(layout)