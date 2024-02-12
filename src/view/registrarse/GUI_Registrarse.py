from PyQt6.QtWidgets import QMainWindow

from src.view.registrarse.Ui_Registrarse import Ui_Registrarse


class GUI_Registrarse(QMainWindow, Ui_Registrarse):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.controller = None
        self.init()

    def init(self):
        self.limpiar()

        self.btn_continuar.clicked.connect(self.clickContinuar)
        self.btn_regresar.clicked.connect(self.clickRegresar)

    def setController(self, controller):
        self.controller = controller

    def clickContinuar(self):
        self.controller.registrarse(self.field_usuario.text(),
                                    self.field_contrasena.text(),
                                    self.field_confirmar_contrasena.text())

    def clickRegresar(self):
        self.controller.regresar()
        pass

    def limpiar(self):
        self.label_estado.clear()
        self.field_usuario.clear()
        self.field_contrasena.clear()
        self.field_confirmar_contrasena.clear()

    def setEstado(self, estado):
        self.label_estado.setText(estado)