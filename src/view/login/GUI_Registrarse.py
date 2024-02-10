from PyQt6.QtWidgets import QMainWindow

from src.view.login.Ui_Registrarse import Ui_Registrarse


class GUI_Login(QMainWindow, Ui_Registrarse):
    def __init__(self, padre=None):
        super().__init__()
        self.setupUi(self)
