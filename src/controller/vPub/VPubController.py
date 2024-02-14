from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

from src.controller.vMisPub.VMisPubController import VMisPubController
from src.controller.vNuevaPub.VNuevaPubController import VNuevaPubController
from src.patrones.Observer import Observer
from src.view.vMisPub.GUI_VMisPub import GUI_VMisPub
from src.view.vNuevaPub.GUI_VNuevaPub import GUI_VNuevaPub
from src.view.vPubDetalle.GUI_VPubDetalle import GUI_VPubDetalle
from src.view.vPubResumen.GUI_VPubResumen import GUI_VPubResumen


class VPubController(Observer):
    def __init__(self, view, model, padre):
        Observer.__init__(self)
        self.view = view
        self.model = model
        self.padre = padre
        self.usuario = None
        self.vNuevaPubController = None
        self.vNuevaPubView = None
        self.vMisPubView = None
        self.vMisPubController = None
        self.vPubDetalleView = None
        self.cargarCuas()
        self.model.suscribirseCuas(self)

    def actualizar(self):
        self.cargarCuas()

    def setUsuario(self, usuario):
        self.usuario = usuario

    def getIdUsuario(self):
        return self.usuario.getIdUsuario()

    def mostrar(self):
        # cargar cuas a la vista
        #self.view.limpiarWidgets()
        #self.cargarCuas()
        self.view.show()

    def publicar(self):
        """Mostrar ventana para realizar nueva vPub
        """
        if not self.vNuevaPubView:
            self.vNuevaPubView = GUI_VNuevaPub()
        if not self.vNuevaPubController:
            self.vNuevaPubController = VNuevaPubController(self.vNuevaPubView,
                                                           self.model,
                                                           self)
        self.vNuevaPubView.setController(self.vNuevaPubController)
        self.vNuevaPubController.mostrar()
        self.view.hide()

    def mostrarMisPublicaciones(self):
        if not self.vMisPubView:
            self.vMisPubView = GUI_VMisPub()
        if not self.vMisPubController:
            self.vMisPubController = VMisPubController(self.vMisPubView,
                                                       self.model,
                                                       self)
        self.vMisPubView.setController(self.vMisPubController)
        self.vMisPubController.mostrar()
        self.view.hide()

    def cargarCuas(self):
        self.view.limpiarWidgets()
        cuas = self.model.getCuas()
        # Devuelve una lista de objetos de tipo cua
        for cua in cuas:
            # Pasar datos amostrar a string
            id_cua = cua.getIdCua()

            id_usuario = cua.getIdUsuario()
            usuario = self.model.getUsuarioById(id_usuario)

            autor = usuario.getUsername()
            titulo = cua.getTitulo()
            contenido = cua.getContenido()[:20] # Mostrar solo los primeros 20 caracteres
            cuaWidget = GUI_VPubResumen(id_cua, autor, titulo, contenido)
            cuaWidget.setController(self)
            cuaWidget.setStyleSheet("background-color: #f9f9f9;")
            self.view.cargarWidget(cuaWidget)

    def agrandar(self, id_cua):
        """Mostrar una venta detallada con la informacion de la nota
        """
        if not self.vPubDetalleView:
            self.vPubDetalleView = GUI_VPubDetalle()

        self.vPubDetalleView.limpiar()

        # Consultar a la bd por la info de la pub
        cua = self.model.getCuaById(id_cua)

        id_usuario = cua.getIdUsuario()
        # Consultar el username y la fota del usuario
        usuario = self.model.getUsuarioById(id_usuario)
        avatar = self.blob_to_pixmap(usuario.getAvatar(), 64)
        autor = usuario.getUsername()

        titulo = cua.getTitulo()
        contenido = cua.getContenido()
        fecha = cua.getFechaModificacionToString()

        self.vPubDetalleView.cargarCua(avatar, autor, titulo, fecha, contenido)

        if cua.getImagen() is not None: # Publicacion con imagen
            imagen = self.blob_to_pixmap(cua.getImagen(), 128)
            self.vPubDetalleView.setImagen(imagen)
        # Mostrar ventana
        self.vPubDetalleView.show()

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
