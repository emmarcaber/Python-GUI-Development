from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox

class Widget(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QMessageBox")

        hard_button = QPushButton("Hard")
        hard_button.clicked.connect(self.hard_button_clicked)

        layout = QVBoxLayout()
        layout.addWidget(hard_button)

        self.setLayout(layout)

    # Hard
    def hard_button_clicked(self):
        messagebox = QMessageBox()
        
        # Set the attributes of the messagebox
        # This is hard since you will manually create your own messagebox
        messagebox.setMinimumSize(700, 200)
        messagebox.setWindowTitle("MessageTitle")
        messagebox.setText("Something happened")
        messagebox.setInformativeText("Do you want to do something about it?")
        messagebox.setIcon(QMessageBox.Critical)
        messagebox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        messagebox.setDefaultButton(QMessageBox.Ok)

        # Show the message box
        result = messagebox.exec()
        if result == QMessageBox.Ok:
            print("User chose Ok")
        else:
            print("User chose Cancel")