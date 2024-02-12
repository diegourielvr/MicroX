from PyQt6.QtWidgets import QMainWindow
from src.view.vNuevaPub.Ui_VNuevaPub import Ui_VNuevaPub

class GUI_VNuevaPub(QMainWindow, Ui_VNuevaPub):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.controller = None
        self.init()

    def init(self):
        self.label_estado.clear()
        self.btn_eliminar_imagen.setVisible(False)

        self.btn_listo.clicked.connect(self.clickListo)
        self.btn_cancelar.clicked.connect(self.clickCancelar)
        self.btn_subir_imagen.clicked.connect(self.clickSubirImagen)
        self.btn_eliminar_imagen.clicked.connect(self.clickEliminar)

    def setController(self, controller):
        self.controller = controller

    def clickListo(self):
        self.controller.listo(self.field_titulo.text(),
                              self.textArea_contenido.toPlainText())

    def clickCancelar(self):
        self.controller.cancelar()

    def clickSubirImagen(self):
        self.controller.subirImagen()

    def clickEliminar(self):
        self.controller.eliminarImagen()

    def limpiar(self):
        self.field_titulo.clear()
        self.label_estado.clear()
        self.limpiarImagen()
        self.textArea_contenido.clear()

    def limpiarImagen(self):
        self.label_imagen.clear()
        self.btn_eliminar_imagen.setVisible(False)

    def cargarImagen(self, pixmap):
        self.label_imagen.setPixmap(pixmap)
        self.btn_eliminar_imagen.setVisible(True)

    def setEstado(self, estado):
        self.label_estado.setText(estado)


