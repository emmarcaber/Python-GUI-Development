from PySide6.QtWidgets import QMainWindow
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, app):
        super().__init__()

        self.app = app

        self.setupUi(self)
        self.setWindowTitle("Embre Notepad")

        self.mainwindow_signals()

    # Set the Signals
    def mainwindow_signals(self):
        self.actionQuit.triggered.connect(self.app.quit)
        self.actionCopy.triggered.connect(self.textEdit.copy)
        self.actionCut.triggered.connect(self.textEdit.cut)
        self.actionPaste.triggered.connect(self.textEdit.paste)
        self.actionUndo.triggered.connect(self.textEdit.undo)
        self.actionRedo.triggered.connect(self.textEdit.redo)