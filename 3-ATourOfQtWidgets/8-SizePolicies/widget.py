from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel, QSizePolicy

class Widget(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Size Policy Demo")

        # Size Policy   :   How the widgets behaves if container space is expanded or shrunk.
        label = QLabel("Some text: ")
        line_edit = QLineEdit()

        # Simulating the defaults. Show vertical expanding
        line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        # line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)     # Make the line edit expand vertically

        # Make the label expand horizontally
        # label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)


        h_layout_1 = QHBoxLayout()
        h_layout_1.addWidget(label)
        h_layout_1.addWidget(line_edit)

        button1 = QPushButton("One")
        button2 = QPushButton("Two")
        button3 = QPushButton("Three")

        # stretch: how much of the available space (in the layout) is occupied by each widget
        # You specify the stretch when you add things to the layout: button1 takes up two (2) units,
        # button2 and button3 takes up one (1) unit
        
        h_layout_2 = QHBoxLayout()
        h_layout_2.addWidget(button1, 2)
        h_layout_2.addWidget(button2, 1)
        h_layout_2.addWidget(button3, 1)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout_1)
        v_layout.addLayout(h_layout_2)

        self.setLayout(v_layout)