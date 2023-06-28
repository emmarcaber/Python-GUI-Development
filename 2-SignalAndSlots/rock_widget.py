from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QHBoxLayout, QVBoxLayout
import sys

class RockWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RockWidget")

        button1 = QPushButton("BUTTON1")
        button1.clicked.connect(self.button1_clicked)

        button2 = QPushButton("BUTTON2")
        button2.clicked.connect(self.button2_clicked)

        widget_layout = QHBoxLayout()   # Horizontal
        # widget_layout = QVBoxLayout()   # Vertical
        widget_layout.addWidget(button1)
        widget_layout.addWidget(button2)

        self.setLayout(widget_layout)

    def button1_clicked(self):
        print("Button1 is clicked!")

    def button2_clicked(self):
        print("Button2 is clicked!")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = RockWidget()
    widget.show()

    app.exec()