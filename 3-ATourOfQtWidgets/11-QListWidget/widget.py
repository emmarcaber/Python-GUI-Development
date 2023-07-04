from PySide6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QAbstractItemView, QPushButton

class Widget(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QListWidget Demo")

        self.list_widget = QListWidget(self)

        # self.list_widget.setSelectionMode(QAbstractItemView.MultiSelection)       # Multi Selection of Items
        self.list_widget.setSelectionMode(QAbstractItemView.SingleSelection)        # Single Selection of Items

        # Adding Default Items to QListWidget
        self.list_widget.addItem("One")
        self.list_widget.addItems(["Two", "Three"])

        # QListWidget Signals
        self.list_widget.currentItemChanged.connect(self.current_item_changed)
        self.list_widget.currentTextChanged.connect(self.current_text_changed)
        
        button_add_item = QPushButton("Add Item")
        button_add_item.clicked.connect(self.add_item)

        button_delete_item = QPushButton("Delete Item")
        button_delete_item.clicked.connect(self.delete_item)

        button_item_count = QPushButton("Item Count")
        button_item_count.clicked.connect(self.item_count)

        button_selected_items = QPushButton("Selected Items")
        button_selected_items.clicked.connect(self.selected_items)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.list_widget)
        v_layout.addWidget(button_add_item)
        v_layout.addWidget(button_delete_item)
        v_layout.addWidget(button_item_count)
        v_layout.addWidget(button_selected_items)

        self.setLayout(v_layout)


    #SLOTS

    # Current Item Changed Slot
    def current_item_changed(self, item):
        print("Current Item:", item.text())

    # Current Text Changed Slot
    def current_text_changed(self, text):
        print("Current Text Changed:", text)
        
    # Add Item Slot
    def add_item(self):
        self.list_widget.addItem("New Item")

    # Delete Item Slot
    def delete_item(self):
        self.list_widget.takeItem(self.list_widget.currentRow())

    # Item Count Slot
    def item_count(self):
        print("Total Items:", self.list_widget.count())

    # Selected Items Slot
    def selected_items(self):
        for items in self.list_widget.selectedItems():
            print(items.text())