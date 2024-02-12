from PyQt6.QtWidgets import QMainWindow

from src.view.login.Ui_Login import Ui_Login


class GUI_Login(QMainWindow, Ui_Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.controller = None
        self.init()

    def init(self):
        self.label_estado.setText("")

        # Manejadores
        self.btn_login.clicked.connect(self.clickLogin)
        self.btn_registrate.clicked.connect(self.clickRegistrarse)

    def setController(self, controller):
        self.controller = controller

    def clickLogin(self):
        self.controller.login(self.field_usuario.text(),
                                   self.field_contrasena.text())

    def setEstado(self, estado):
        self.label_estado.setText(estado)

    def clickRegistrarse(self):
        self.controller.registrarse()

    def limpiarCampos(self):
        self.field_usuario.clear()
        self.field_contrasena.clear()
        self.label_estado.clear()
