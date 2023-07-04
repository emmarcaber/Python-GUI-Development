from PySide6.QtWidgets import QWidget, QPushButton, QComboBox, QHBoxLayout, QVBoxLayout, QGroupBox

class Widget(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QComboBox Demo")

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.planets_groupbox())

        self.setLayout(main_layout)

    # Planets GroupBox
    def planets_groupbox(self):
        group_box = QGroupBox("Choose a planet")
        self.combo_box = QComboBox()

        # Add Planets to the ComboBox
        self.combo_box.addItem("Mercury")
        self.combo_box.addItem("Venus")
        self.combo_box.addItem("Earth")
        self.combo_box.addItem("Mars")
        self.combo_box.addItem("Jupiter")
        self.combo_box.addItem("Saturn")
        self.combo_box.addItem("Uranus")

        # Buttons
        button_current_value = QPushButton("Current Value")
        button_current_value.clicked.connect(self.current_value)
        
        button_set_current = QPushButton("Set Value")
        button_set_current.clicked.connect(self.set_current)

        button_get_values = QPushButton("Get Values")
        button_get_values.clicked.connect(self.get_values)
        

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.combo_box)
        v_layout.addWidget(button_current_value)
        v_layout.addWidget(button_set_current)
        v_layout.addWidget(button_get_values)

        group_box.setLayout(v_layout)

        return group_box


    # SLOTS
        
    # Current Value Slot
    def current_value(self):
        print(f"Current Item: {self.combo_box.currentText()} - Current Index: {self.combo_box.currentIndex()}")

    # Set Current Slot
    def set_current(self):
        self.combo_box.setCurrentIndex(2)
        
    # Get Values Slot
    def get_values(self):
        for i in range(self.combo_box.count()):
            print(f"Index [{i}]: {self.combo_box.itemText(i)}")



