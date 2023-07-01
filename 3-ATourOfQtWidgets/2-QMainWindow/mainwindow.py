from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar

class MainWindow(QMainWindow):

    def __init__(self, app):
        super().__init__()
        self.app = app  # declare an app member
        self.setWindowTitle("Custom MainWindow")

        self.menubars_and_menus() # Add the menubars and menus
        self.toolbars()
        self.statusbar()

        button1 = QPushButton("BUTTON1")
        button1.clicked.connect(self.button1_clicked)
        self.setCentralWidget(button1)

    # Menubars and Menus
    def menubars_and_menus(self):        
        menubar = self.menuBar()

        # NOTE: The ampersand enables the 
        # pressing ALT+ the mnemonic character to set the focus to the control 
        # that follows the Label in the tab order of the menus and MenuBar
        file_menu = menubar.addMenu("&File")
        self.quit_action = file_menu.addAction("Quit")
        self.quit_action.triggered.connect(self.quit_app)
    
        edit_menu = menubar.addMenu("&Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")
    
        menubar.addMenu("&Window")
        menubar.addMenu("&Setting")
        menubar.addMenu("&Help")

    # Working with toolbars
    def toolbars(self):
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)
    
        # Add the quit action to the toolbar
        toolbar.addAction(self.quit_action)
    
        action1 = QAction("Some action", self)
        action1.setStatusTip("Status message for some action")
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)

        action2 = QAction(QIcon("start.png"), "Some other action", self)
        action2.setStatusTip("Status message for some other action")
        action2.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action2)

        toolbar.addSeparator()
        toolbar.addWidget(QPushButton("Click here"))
    
    # Working with status bars
    def statusbar(self):
        self.setStatusBar(QStatusBar(self))
    
    def button1_clicked(self):
        print("Button is clicked")
        
    def toolbar_button_click(self):
        self.statusBar().showMessage("Message for my app", 3000)

    def quit_app(self):
        self.app.quit()