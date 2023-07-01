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
        file_menu = menubar.addMenu("&File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)

    def quit_app(self):
        self.app.quit()