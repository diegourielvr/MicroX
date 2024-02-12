from PyQt6.QtWidgets import QWidget

from src.view.vMiPub.Ui_VMiPub import Ui_VMiPub


class GUI_VMiPub(QWidget, Ui_VMiPub):
    def __init__(self, id_cua, titulo, contenido, fecha_modificacion):
        """Crea un widget que muestra el contenido del cua
        id_cua: int
        titulo: str
        contenido: str
        fecha_modificacion: str
        """
        super().__init__()
        self.setupUi(self)
        self.id_cua = id_cua
        self.label_titulo.setText(titulo)
        self.textArea_contenido.setText(contenido)
        self.label_fecha_modificacion.setText(fecha_modificacion)
        self.init()

    def init(self):
        self.btn_editar.clicked.connect(self.clickEditar)
        self.btn_eliminar.clicked.connect(self.clickEliminar)

    def setController(self, controller):
        self.controller = controller

    def clickEditar(self):
        self.controller.editar(self.id_cua)

    def clickEliminar(self):
        self.controller.eliminar(self.id_cua)

    def setImagen(self, imagen):
        self.label_imagen.setPixmap(imagen)
