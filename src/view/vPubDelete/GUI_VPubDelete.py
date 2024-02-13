from PyQt6.QtWidgets import QMainWindow

from src.view.vPubDelete.Ui_VPubDelete import Ui_VPubDelete


class GUI_VPubDelete(QMainWindow, Ui_VPubDelete):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.controller = None
        self.init()

    def init(self):
        self.btn_cancelar.clicked.connect(self.clickCancelar)
        self.btn_eliminar.clicked.connect(self.clickEliminar)

    def setController(self, controller):
        self.controller = controller

    def clickEliminar(self):
        self.controller.eliminar()

    def clickCancelar(self):
        self.controller.cancelar()