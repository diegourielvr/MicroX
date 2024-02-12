from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QFileDialog


class VNuevaPubController:
    def __init__(self, view, model, padre):
        self.view = view
        self.model = model
        self.padre = padre
        self.path_img = None
        self.MAX_NUM_PALABRAS = 50

    def mostrar(self):
        self.view.show()

    def listo(self, titulo, contenido):
        # Verificaar si esta vacio titulo o contenido
        if not titulo or titulo.isspace() or not contenido or contenido.isspace():
            self.view.setEstado("Campos vacios")
            return

        # Eliminar espacios al inicio y al final
        titulo = titulo.strip()
        contenido = contenido.strip()

        # Validar que solo pueda escribir 50 palabras maximo
        num_palabras = len(contenido.split())
        if num_palabras > self.MAX_NUM_PALABRAS:
            self.view.setEstado(f"{num_palabras}/50")
            return

        img_data = None
        if self.path_img:
            # convertir la imagen a binario para guardar
            with open(self.path_img, "rb") as file:
                img_data = file.read()
        # Solicitar el id_usuario al padre
        id_usuario = self.padre.getIdUsuario()
        self.model.agregarCua(id_usuario, titulo, contenido, img_data)
        self.padre.mostrar()
        self.view.limpiar()
        self.view.hide()

    def cancelar(self):
        # Limpiar campos de la vista VNuevaPub
        self.view.limpiar()
        self.path_img = None
        self.view.hide()
        self.padre.mostrar()

    def subirImagen(self):
        file_dialog= QFileDialog()
        file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg)")
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        if file_dialog.exec():
            file_path = file_dialog.selectedFiles()[0] # Seleccionar el primer archivo
            self.path_img = file_path
            self.agregarImagen(file_path)

    def agregarImagen(self, path):
        pixmap = QPixmap(path)
        if not pixmap.isNull():
            pixmap = pixmap.scaled(128, 128, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
            self.view.cargarImagen(pixmap)

    def eliminarImagen(self):
        self.path_img = None
        self.view.limpiarImagen()