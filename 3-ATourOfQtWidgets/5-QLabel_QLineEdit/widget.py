from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit

class Widget(QWidget):

    def __init__(self):
        super().__init__()

        label = QLabel("Full Name: ")
        self.line_edit = QLineEdit()
        # self.line_edit.textChanged.connect(self.text_changed)
        # self.line_edit.cursorPositionChanged.connect(self.cursor_position_changed)
        # self.line_edit.editingFinished.connect(self.editing_finished)
        self.line_edit.returnPressed.connect(self.return_pressed)
        # self.line_edit.selectionChanged().connect(self.selection_changed)
        self.line_edit.textEdited.connect(self.text_edited)


        submit_button = QPushButton("SUBMIT")
        submit_button.clicked.connect(self.submit_button_clicked)
        
        self.fullname_holder_label = QLabel("I am HERE")

        # Horizontal Layout
        # Full Name Label and QLineEdit
        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)

        # Vertical Layout
        # For Horizontal Layout and Other Widgets
        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(submit_button)
        v_layout.addWidget(self.fullname_holder_label)

        self.setLayout(v_layout)


    # SLOTS
    def submit_button_clicked(self):
        print("Full Name:", self.line_edit.text())
        self.fullname_holder_label.setText(self.line_edit.text())

    # When the text in QLineEdit is being edited, this slot receives
    def text_changed(self):
        print("Text changed to:", self.line_edit.text())
        self.fullname_holder_label.setText(self.line_edit.text())

    # When the text in QLineEdit is being edited, this slot receives
    def cursor_position_changed(self, old, new):
        print("Cursor Old Position:", old, " New Position:", new)

    # When the window is closed, this slot receives
    def editing_finished(self):
        print("Editing finished")

    # When editing the QLineEdit, you entered. This slot receives
    def return_pressed(self):
        print("Full Name:", self.line_edit.text())
        self.fullname_holder_label.setText(self.line_edit.text())

    # Not functioning well
    def selection_changed(self):
        print("Selection Changed:", self.line_edit.selectedText())

    # When the text in QLineEdit is being edited, this slot receives
    def text_edited(self, new_text):
        print("Text edited. New text:", new_text)

    

    