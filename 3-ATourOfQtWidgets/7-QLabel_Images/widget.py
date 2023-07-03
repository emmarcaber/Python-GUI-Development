from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class Widget(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLabel Images Demo")

        image_label = QLabel()
        image_label.setPixmap(QPixmap("images/minions.png"))

        layout = QVBoxLayout()
        layout.addWidget(image_label)

        self.setLayout(layout)