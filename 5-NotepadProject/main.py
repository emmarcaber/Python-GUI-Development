"""
    You can download icons in icons8.com for free.
"""

import sys

from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow(app)
    window.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print("Closing Window")

