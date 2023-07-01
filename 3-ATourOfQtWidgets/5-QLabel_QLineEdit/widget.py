from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit

class Widget(QWidget):

    def __init__(self):
        super().__init__()

        label = QLabel("Full Name: ")
        self.line_edit = QLineEdit()

        submit_button = QPushButton("SUBMIT")
        submit_button.clicked.connect(self.submit_button_clicked)
        
        self.fullname_holder_label = QLabel("I am HERE")

        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(submit_button)
        v_layout.addWidget(self.fullname_holder_label)

        self.setLayout(v_layout)

    def submit_button_clicked(self):
        print("Full Name:", self.line_edit.text())
        self.fullname_holder_label.setText(self.line_edit.text())