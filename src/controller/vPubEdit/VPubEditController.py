from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QFileDialog


class VPubEditController:
    def __init__(self, view, model, padre):
        self.view = view
        self.model = model
        self.padre = padre
        self.cua = None
        self.new_path_img = None
        self.modificar_imagen = False
        self.MAX_NUM_PALABRAS = 50

    def cargarCuaById(self, id_cua):
        # Consultar a la base de datos y cargar todos los datos en la vista
        self.cua = self.model.getCuaById(id_cua)
        self.view.cargarCua(self.cua.getTitulo(), self.cua.getContenido())
        if self.cua.getImagen() is not None:
            self.view.cargarImagen(self.blob_to_pixmap(self.cua.getImagen(), 128))
            self.view.mostrarEliminarImagen()

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
        if self.new_path_img:
            # convertir la imagen a binario para guardar
            with open(self.new_path_img, "rb") as file:
                img_data = file.read()
        elif self.modificar_imagen:
            img_data = None
        else:
            img_data = self.cua.getImagen()
        self.model.modificarCuaById(self.cua.getIdCua(),
                                    titulo,
                                    contenido,
                                    img_data)
        self.padre.mostrarPadre()
        self.view.limpiar()
        self.view.hide()

    def cancelar(self):
        self.view.limpiar()
        self.view.hide()
        self.padre.mostrar()

    def subirImagen(self):
        file_dialog= QFileDialog()
        file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg)")
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        if file_dialog.exec():
            file_path = file_dialog.selectedFiles()[0] # Seleccionar el primer archivo
            self.new_path_img = file_path
            self.agregarImagen(self.new_path_img)

    def agregarImagen(self, path):
        pixmap = QPixmap(path)
        if not pixmap.isNull():
            pixmap = pixmap.scaled(128, 128, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
            self.view.cargarImagen(pixmap)

    def eliminarImagen(self):
        self.new_path_img = None
        self.modificar_imagen = True
        self.view.limpiarImagen()

    def mostrar(self):
        self.view.show()

    def blob_to_pixmap(self, blob, size):
        if not blob:
            return None

        try:
            pixmap = QPixmap()
            pixmap.loadFromData(blob)
            if not pixmap.isNull():
                pixmap = pixmap.scaled(size, size, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
            return pixmap
        except Exception as e:
            print("Error al convertir blob a QPixmap")
            return None
