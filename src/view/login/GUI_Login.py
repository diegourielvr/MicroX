from PyQt6.QtWidgets import QMainWindow

from src.view.login.Ui_Login import Ui_Login


class GUI_Login(QMainWindow, Ui_Login):
    def __init__(self, padre=None):
        super().__init__()
        self.setupUi(self)