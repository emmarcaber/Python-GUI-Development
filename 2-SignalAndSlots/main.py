# VERSION 1 :   Just responding to the button click : syntax
"""
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

# ANOTHER NOTE: You can find the signal of a widget
                in the documentation, if not found,
                it is in their parent class
"""

# VERSION 2 :   SIGNALS SENDING VALUES, SLOTS CAPTURE THE VALUES
"""
from PySide6.QtWidgets import QApplication, QPushButton


# The slot  : responds when something happens
def button_clicked(data):
    print("You clicked the button, didn't you! checked : ", data)


app = QApplication()
button = QPushButton("Press Me")
button.setCheckable(True)  # Makes the button checkable. It's unchecked by default.
# Further clicks the toggle between checked and unchecked states

# clicked is a signal of the QPushButton. It's emitted when you click on the button
# You can wire a slot to the signal using the syntax below:
button.clicked.connect(button_clicked)

button.show()
app.exec()
"""


# VERSION3  :   CAPTURE VALUE FROM A SLIDER - OTHER EXAMPLE

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider


# The slot  : responds when something happens
def respond_to_slider(data):
    print("slider moved to  :  ", data)


app = QApplication()
slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)

# You just do the connection. The Qt system takes care of
# passing the data from the signal to the slot.
slider.valueChanged.connect(respond_to_slider)
slider.show()

app.exec()
