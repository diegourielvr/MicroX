from base64 import b64decode

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMessageBox

from src.controller.vPubDelete.VPubDeleteController import VPubDeleteController
from src.controller.vPubEdit.VPubEditController import VPubEditController
from src.patrones.Observer import Observer
from src.view.vMiPub.GUI_VMiPub import GUI_VMiPub
from src.view.vPubDelete.GUI_VPubDelete import GUI_VPubDelete
from src.view.vPubEdit.GUI_VPubEdit import GUI_VPubEdit


class VMisPubController(Observer):
    def __init__(self, view, model, padre):
        Observer.__init__(self)
        self.view = view
        self.model = model
        self.padre = padre
        self.vPubEditView = None
        self.vPubEditController = None
        self.vPubDeleteView = None
        self.vPubDeleteController = None
        self.cargarMisCuas()
        self.model.suscribirseCuas(self)

    def actualizar(self):
        self.cargarMisCuas()

    def regresar(self):
        self.padre.mostrar()
        self.view.hide()

    def editar(self, id_cua):
        if not self.vPubEditView:
            self.vPubEditView = GUI_VPubEdit()
        if not self.vPubEditController:
            self.vPubEditController = VPubEditController(self.vPubEditView,
                                                         self.model,
                                                         self)
        self.vPubEditView.setController(self.vPubEditController)
        self.vPubEditController.cargarCuaById(id_cua)
        self.vPubEditController.mostrar()
        self.view.hide()

    def eliminar(self, id_cua):
        if not self.vPubDeleteView:
            self.vPubDeleteView = GUI_VPubDelete()
        if not self.vPubDeleteController:
            self.vPubDeleteController = VPubDeleteController(self.vPubDeleteView,
                                                             self.model,
                                                             self)
        self.vPubDeleteView.setController(self.vPubDeleteController)
        self.vPubDeleteController.setIdCua(id_cua)
        self.vPubDeleteController.mostrar()
        self.view.hide()

    def cargarMisCuas(self):
        self.view.limpiarWidgets()
        # Obtener cuas del model en orden descendent
        cuas = self.model.getCuasByIdUsuario(self.padre.getIdUsuario())
        if not cuas:
            return

        #Crear objetos de tipo miPub
        for cua in cuas:
            id_cua = cua.getIdCua() # int
            titulo = cua.getTitulo() # str
            contenido = cua.getContenido() # str
            fecha_modificacion = cua.getFechaModificacionToString()
            cuaWidget = GUI_VMiPub(id_cua, titulo, contenido, fecha_modificacion)
            if cua.getImagen() is not None:
                imagen = self.blob_to_pixmap(cua.getImagen(), 128) # bytes
                cuaWidget.setImagen(imagen)

            cuaWidget.setController(self)
            self.view.cargarWidget(cuaWidget)

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

    def mostrar(self):
        #self.view.limpiarWidgets()
        #self.cargarMisCuas()
        self.view.show()

    def mostrarPadre(self):
        self.view.hide()
        self.padre.mostrar()