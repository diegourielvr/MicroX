from PyQt6.QtWidgets import QMainWindow

from src.view.vPubEdit.Ui_VPubEdit import Ui_VPubEdit


class GUI_VPubEdit(QMainWindow, Ui_VPubEdit):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.controller = None
        self.init()

    def init(self):
        self.limpiar()
        self.btn_listo.clicked.connect(self.clickListo)
        self.btn_cancelar.clicked.connect(self.clickCancelar)
        self.btn_subir_imagen.clicked.connect(self.clickSubirImagen)
        self.btn_eliminar_imagen.clicked.connect(self.clickEliminarImagen)

    def cargarCua(self, titulo, contenido):
        self.field_titulo.setText(titulo)
        self.textArea_contenido.setText(contenido)

    def cargarImagen(self, pixmap):
        self.label_imagen.setPixmap(pixmap)
        self.btn_eliminar_imagen.setVisible(True)

    def mostrarEliminarImagen(self):
        self.btn_eliminar_imagen.setVisible(True)

    def clickListo(self):
        self.controller.listo(self.field_titulo.text(),
                              self.textArea_contenido.toPlainText())

    def clickCancelar(self):
        self.controller.cancelar()

    def clickSubirImagen(self):
        self.controller.subirImagen()

    def clickEliminarImagen(self):
        self.controller.eliminarImagen()

    def setController(self, controller):
        self.controller = controller

    def limpiarImagen(self):
        self.label_imagen.clear()
        self.btn_eliminar_imagen.setVisible(False)

    def limpiar(self):
        self.limpiarImagen()
        self.field_titulo.clear()
        self.textArea_contenido.clear()
        self.label_estado.setText("")
        self.btn_eliminar_imagen.setVisible(False)