# Import the necessary files
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QHBoxLayout, QVBoxLayout
import sys

# RockWidget class inherits from QWidget
class RockWidget(QWidget):
    
    # Constructor Method
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RockWidget")                   # Set the Window Title

        # Create button1
        button1 = QPushButton("BUTTON1")
        button1.clicked.connect(self.button1_clicked)       # Set the signal for button1

        # Create button2
        button2 = QPushButton("BUTTON2")
        button2.clicked.connect(self.button2_clicked)       # Set the signal for button2

        # Create the layout
        widget_layout = QHBoxLayout()   # Horizontal
        # widget_layout = QVBoxLayout()   # Vertical
    
        # Add the two buttons into the layout
        widget_layout.addWidget(button1)
        widget_layout.addWidget(button2)

        self.setLayout(widget_layout)

    # Slot method when button1 is clicked
    def button1_clicked(self):
        print("Button1 is clicked!")

    
    # Slot method when button2 is clicked
    def button2_clicked(self):
        print("Button2 is clicked!")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = RockWidget()
    widget.show()

    app.exec()