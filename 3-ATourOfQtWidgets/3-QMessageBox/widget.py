from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox

class Widget(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QMessageBox")

        hard_button = QPushButton("Hard")
        hard_button.clicked.connect(self.hard_button_clicked)
        
        critical_button = QPushButton("Critical")
        critical_button.clicked.connect(self.critical_button_clicked)

        question_button = QPushButton("Question")
        question_button.clicked.connect(self.question_button_clicked)

        information_button = QPushButton("Information")
        information_button.clicked.connect(self.information_button_clicked)

        warning_button = QPushButton("Warning")
        warning_button.clicked.connect(self.warning_button_clicked)

        about_button = QPushButton("About")
        about_button.clicked.connect(self.about_button_clicked)

        layout = QVBoxLayout()
        layout.addWidget(hard_button)
        layout.addWidget(critical_button)
        layout.addWidget(question_button)
        layout.addWidget(information_button)
        layout.addWidget(warning_button)
        layout.addWidget(about_button)

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

    # Critical
    def critical_button_clicked(self):
        result = QMessageBox.critical(self, "Critical MessageBox", "This is a critical message! \nDo you want to continue?", QMessageBox.Ok | QMessageBox.Cancel)

        if result == QMessageBox.Ok:
            print("User chose Ok")
        else:
            print("User chose Cancel")

    # Question
    def question_button_clicked(self):
        result = QMessageBox.question(self, "Question MessageBox", "Asking a question?", QMessageBox.Ok | QMessageBox.Cancel)

        if result == QMessageBox.Ok:
            print("User chose Ok")
        else:
            print("User chose Cancel")

    # Information
    def information_button_clicked(self):
        result = QMessageBox.information(self, "Information MessageBox", "This is an informative text", QMessageBox.Ok | QMessageBox.Cancel)

        if result == QMessageBox.Ok:
            print("User chose Ok")
        else:
            print("User chose Cancel")

    # Warning
    def warning_button_clicked(self):
        result = QMessageBox.warning(self, "Warning MessageBox", "Caution! This is a warning message!", QMessageBox.Ok | QMessageBox.Cancel)

        if result == QMessageBox.Ok:
            print("User chose Ok")
        else:
            print("User chose Cancel")

    # About
    def about_button_clicked(self):
        result = QMessageBox.about(self, "About MessageBox", "Some about message")

        if result == QMessageBox.Ok:
            print("User chose Ok")
        else:
            print("User chose Cancel")