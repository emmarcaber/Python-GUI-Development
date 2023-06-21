# VERSION 1 :   Just responding to the button click : syntax
from PySide6.QtWidgets import QApplication, QPushButton


# The slot : responds when something happens
# When you do some Javascript, remember it like function of the event listener
def button_clicked():
    print("You clicked the button, didn't you?")


app = QApplication()
button = QPushButton("Press Me")

# clicked : is a signal of QPushButton. It's emitted when you click
#           on the button
# You can wire a slot to the signal using the syntax below:
button.clicked.connect(button_clicked)

button.show()
app.exec()

# NOTE: Simply put that the SIGNAL is the event listener
#       and the SLOT is the function when the event happens
