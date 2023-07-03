from PySide6.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QCheckBox

class Widget(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QCheckbox and QRadioButton")

        # Layout for First Two Groupboxes
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.os_groupbox())
        h_layout.addWidget(self.drink_groupbox())

        layout = QVBoxLayout()
        layout.addLayout(h_layout)
        layout.addWidget(self.answers_groupbox())
        
        self.setLayout(layout)


    # OS Groupbox
    def os_groupbox(self):
        mac = QCheckBox("Mac")
        mac.toggled.connect(self.mac_checkbox_toggled)

        windows = QCheckBox("Window")
        windows.toggled.connect(self.windows_checkbox_toggled)

        linux = QCheckBox("Linux")
        linux.toggled.connect(self.linux_checkbox_toggled)

        os = QGroupBox("Choose an operating system")

        os_layout = QVBoxLayout()
        os_layout.addWidget(mac)
        os_layout.addWidget(windows)
        os_layout.addWidget(linux)

        os.setLayout(os_layout)

        return os


    # Drinks Groupbox
    def drink_groupbox(self):
        drinks = QGroupBox("Choose your drinks")

        beer = QCheckBox("Beer")
        juice = QCheckBox("Juice")
        coffee = QCheckBox("Coffee")
        beer.setChecked(True)

        # Make the checkboxes exclusive
        exclusive_button_group = QButtonGroup(self)     # The self parent is needed here
        exclusive_button_group.addButton(beer)
        exclusive_button_group.addButton(juice)
        exclusive_button_group.addButton(coffee)
        exclusive_button_group.setExclusive(True)
        
        drinks_layout = QVBoxLayout()
        drinks_layout.addWidget(beer)
        drinks_layout.addWidget(juice)
        drinks_layout.addWidget(coffee)

        drinks.setLayout(drinks_layout)

        return drinks
    

    # Answers Groupbox
    def answers_groupbox(self):
        answers = QGroupBox("Choose Answer")

        answer_a = QRadioButton("A")
        answer_b = QRadioButton("B")
        answer_c = QRadioButton("C")

        answers_layout = QVBoxLayout()
        answers_layout.addWidget(answer_a)
        answers_layout.addWidget(answer_b)
        answers_layout.addWidget(answer_c)

        answers.setLayout(answers_layout)

        return answers


    # SLOTS FOR OS CHECKBOXES

    # Mac Checkbox Toggled
    def mac_checkbox_toggled(self, checked):
        if (checked):
            print("Max box checked")
        else:
            print("Mac box unchecked")
    
    # Windows Checkbox Toggled
    def windows_checkbox_toggled(self, checked):
        if (checked):
            print("Windows box checked")
        else:
            print("Windows box unchecked")
    
    # Linux Checkbox Toggled
    def linux_checkbox_toggled(self, checked):
        if (checked):
            print("Linux box checked")
        else:
            print("Linux box unchecked")