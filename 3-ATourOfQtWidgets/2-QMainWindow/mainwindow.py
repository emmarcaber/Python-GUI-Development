from PySide6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):

    def __init__(self, app):
        super().__init__()
        self.app = app  # declare an app member
        self.setWindowTitle("Custom MainWindow")

        self.menubars_and_menus()

    # Menubars and Menus
    def menubars_and_menus(self):        
        menubar = self.menuBar()

        # NOTE: The ampersand enables the 
        # pressing ALT+ the mnemonic character to set the focus to the control 
        # that follows the Label in the tab order of the menus and MenuBar
        file_menu = menubar.addMenu("&File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)
    
        edit_menu = menubar.addMenu("&Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")
    
        menubar.addMenu("&Window")
        menubar.addMenu("&Setting")
        menubar.addMenu("&Help")

    def quit_app(self):
        self.app.quit()