from PyQt6.QtWidgets import QMainWindow

from src.view.publicacion.Ui_VPub import Ui_VPub


class GUI_VPub(QMainWindow, Ui_VPub):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.controller = None
        #self.init()

    def init(self):
        return

    def setController(self, controller):
        self.controller = controller