from PySide6.QtWidgets import QTabWidget, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QWidget

class Widget(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTabWidget Demo")

        tab_widget = QTabWidget(self)

        # Add the Tabs of QTabWidget
        # Each tab is a QWidget
        tab_widget.addTab(self.widget_form(), "Information")
        tab_widget.addTab(self.widget_buttons(), "Buttons")

        main_layout = QVBoxLayout()
        main_layout.addWidget(tab_widget)

        self.setLayout(main_layout)

    # Widget Form
    def widget_form(self):
        widget = QWidget()

        label = QLabel("Full Name: ")
        line_edit = QLineEdit()

        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(line_edit)

        widget.setLayout(h_layout)

        return widget

    # Widget Buttons
    def widget_buttons(self):
        widget = QWidget()

        button_1 = QPushButton("One")
        button_1.clicked.connect(self.button_1_clicked)

        button_2 = QPushButton("Two")
        button_3 = QPushButton("Three")

        v_layout = QVBoxLayout()
        v_layout.addWidget(button_1)
        v_layout.addWidget(button_2)
        v_layout.addWidget(button_3)

        widget.setLayout(v_layout)

        return widget

    # Button 1 Slot
    def button_1_clicked(self):
        print("Button 1 Clicked")