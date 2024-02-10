from PyQt6.QtWidgets import QMainWindow

from src.view.login.Ui_Avatar import Ui_Avatar


class GUI_Login(QMainWindow, Ui_Avatar):
    def __init__(self, padre=None):
        super().__init__()
        self.setupUi(self)
