from src.controller.login.LoginController import LoginController
from src.controller.vPub.VPubController import VPubController
from src.controller.registrarse.RegistrarseController import RegistrarseController
from src.model.Conexion import Conexion
from src.view.login.GUI_Login import GUI_Login
from src.view.vPub.GUI_VPub import GUI_VPub
from src.view.registrarse.GUI_Registrarse import GUI_Registrarse


class MasterController:
    def __init__(self):
        self.usuario = None
        self.dbModel = Conexion()

        self.loginView = None
        self.loginController = None
        self.registrarseView = None
        self.registrarseController = None
        self.vPubView = None
        self.vPubController = None
    def mostrarLogin(self):
        """Mostrar interfaz para hacer login

        """
        if not self.loginView:
            self.loginView = GUI_Login()
        if not self.loginController:
            self.loginController = LoginController(self.loginView,
                                                   self.dbModel,
                                                   self)
        self.loginView.setController(self.loginController)
        self.loginController.mostrar()

    def setUsuario(self, usuario):
        """Usuario del estado actual

        :param usuario: Usuario
        """
        self.usuario = usuario

    def mostrarRegistrarse(self):
        if not self.registrarseView:
            self.registrarseView = GUI_Registrarse()
        if not self.registrarseController:
            self.registrarseController = RegistrarseController(self.registrarseView,
                                                               self.dbModel,
                                                               self)
        self.registrarseView.setController(self.registrarseController)
        self.registrarseController.mostrar()

    def mostrarVPub(self):
        if not self.vPubView:
            self.vPubView = GUI_VPub()
        if not self.vPubController:
            self.vPubController = VPubController(self.vPubView,
                                                 self.dbModel,
                                                 self)
        self.vPubView.setController(self.vPubController)
        self.vPubController.setUsuario(self.usuario)
        self.vPubController.mostrar()
