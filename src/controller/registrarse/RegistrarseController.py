import os

from PyQt6.QtCore import Qt, QFileInfo
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QFileDialog, QLabel, QMessageBox

from src.view.registrarse.avatar.GUI_Avatar import GUI_Avatar
class RegistrarseController:
    def __init__(self, view, model, padre):
        self.view = view
        self.model = model
        self.padre = padre
        self.username = None
        self.password = None
        self.avatarView = None
        self.path_avatar = None

    def mostrar(self):
        self.view.show()

    def registrarse(self, usuario, contrasena, confirmar_contrasena):
        """

        :param usuario:
        :param contrasena:
        :param confirmar_contrasena:
        :return:
        """
        if not usuario or not contrasena or not confirmar_contrasena:
            self.view.setEstado("Llena los campos")
            return
        # Validar si contrasena y confirmar_contrasena son iguales
        if contrasena != confirmar_contrasena:
            self.view.setEstado("Contraseña incorrecta")
            return
        # Validar si el usuari a registrar no existe
        if self.model.existeUsuario(usuario):
            self.view.setEstado("Usuario existente")
            self.view.setEstado("El usuario ya existe")
            return

        self.username = usuario
        self.password = contrasena
        # Llamar a mostrarElegirAvatar para terminar de guardar el usuario
        self.mostrarElegirAvatar()

    def regresar(self):
        self.padre.mostrarLogin()
        self.view.limpiar()
        self.view.hide()

    def mostrarElegirAvatar(self):
        self.view.hide()
        if not self.avatarView:
            self.avatarView = GUI_Avatar()
        self.avatarView.setController(self)
        self.avatarView.show()

    def subirImagen(self):
        # Abrir un cuadro de diálogo para seleccionar imágenes
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg)")
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        if file_dialog.exec():
            file_path = file_dialog.selectedFiles()[0] # Seleccionar el primer archivo
            self.path_avatar = file_path
            self.agregarImagen(file_path)


    def seleccionarImagen(self, full_path):
        self.path_avatar = full_path
        self.agregarImagen(self.path_avatar)

    def guardar(self):
        if not self.path_avatar:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Selecciona un avatar")
            msg_box.setText("Debes seleccionar un avatar para terminar el registro")
            msg_box.exec()
            return
        # NOTE: transformar la imagen a binario
        #avatar_data = None
        with open(self.path_avatar, "rb") as file:
            avatar_data = file.read()
        self.model.agregarUsuario(self.username, self.password, avatar_data)
        self.padre.mostrarLogin()
        self.view.limpiar()
        self.avatarView.hide()

    def quitarImagen(self):
        self.path_avatar = None
        self.avatarView.limpiarImagen()

    def agregarImagen(self, path_avatar):
        pixmap = QPixmap(path_avatar)
        if not pixmap.isNull():
            pixmap = pixmap.scaled(128, 128, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
            self.avatarView.cargarImagen(pixmap)