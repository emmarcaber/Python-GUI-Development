# importing the components we need
from PySide6.QtWidgets import QApplication, QWidget

# sys is a module responsible for processing command-line arguments
import sys

# the arguments inside the command-line
# will be processed by the QApplication
app = QApplication(sys.argv)

# create a new window
# NOTE: By default the windows or widget of QT are hidden,
#       so you need to show it
window = QWidget()
window.show()

# start the application
app.exec()
