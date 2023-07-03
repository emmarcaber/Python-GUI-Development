from PySide6.QtWidgets import QWidget, QTextEdit, QHBoxLayout, QVBoxLayout, QPushButton

class Widget(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTextEdit Demo")

        self.text_edit = QTextEdit()

        # BUTTONS

        # Current Text
        current_text_button = QPushButton("Current Text")
        current_text_button.clicked.connect(self.current_text_button_clicked)

        # Copy
        copy_button = QPushButton("Copy")
        copy_button.clicked.connect(self.text_edit.copy) # Connect directly to QTextEdit Slot

        # Cut
        cut_button = QPushButton("Cut")
        cut_button.clicked.connect(self.text_edit.cut)

        # Undo
        undo_button = QPushButton("Undo")
        undo_button.clicked.connect(self.text_edit.undo)
        
        # Redo
        redo_button = QPushButton("Redo")
        redo_button.clicked.connect(self.text_edit.redo)
        
        # Set Plain Text
        set_plain_text_button = QPushButton("Set Plain Text")
        set_plain_text_button.clicked.connect(self.set_plain_text_button_clicked)
        
        # Set HTML
        set_html_button = QPushButton("Set HTML")
        set_html_button.clicked.connect(self.set_html_button_clicked)

        # Horizontal Layout for Buttons
        h_layout = QHBoxLayout()
        h_layout.addWidget(current_text_button)
        h_layout.addWidget(copy_button)
        h_layout.addWidget(cut_button)
        h_layout.addWidget(undo_button)
        h_layout.addWidget(redo_button)
        h_layout.addWidget(set_plain_text_button)
        h_layout.addWidget(set_html_button)

        # Vertical Layout for all of the Widgets
        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.text_edit)
    
        self.setLayout(v_layout)


    # Current Text Button Slot
    def current_text_button_clicked(self):
        print(self.text_edit.toPlainText())

    # Set Plain Text Button Slot
    def set_plain_text_button_clicked(self):
        self.text_edit.setPlainText("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

    # Set HTML Button Slot
    def set_html_button_clicked(self):
        self.text_edit.setHtml("<h1>Hello, World!</h1> <h2>This is <b>Emmar Caber</b></h2> A <i>Full-Stack Software Engineer</i>")