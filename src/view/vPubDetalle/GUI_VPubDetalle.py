from PyQt6.QtWidgets import QMainWindow

from src.view.vPubDetalle.Ui_VPubDetalle import Ui_VPubDetalle


class GUI_VPubDetalle(QMainWindow, Ui_VPubDetalle):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def cargarCua(self, avatar, autor, titulo, fecha, contenido):
        """
        :param avatar: pixmap
        :param autor: str
        :param titulo: str
        :param fecha: str
        :param contenido: str
        :return:
        """
        self.label_avatar.setPixmap(avatar)
        self.label_autor.setText(autor)
        self.label_titulo.setText(titulo)
        self.label_fecha_modificacion.setText(fecha)
        self.textArea_contenido.setText(contenido)

    def setImagen(self, imagen):
        #:param imagen: Pixmap
        self.label_imagen.setPixmap(imagen)

    def limpiar(self):
        self.label_avatar.clear()
        self.label_autor.clear()
        self.label_titulo.clear()
        self.label_fecha_modificacion.clear()
        self.textArea_contenido.clear()
        self.label_imagen.clear()
