from PyQt6.QtWidgets import QMainWindow, QWidget
from src.view.vPubResumen.Ui_VPubResumen import Ui_VPubResumen


class GUI_VPubResumen(QWidget, Ui_VPubResumen):
    def __init__(self, id_cua, autor, titulo, contenido):
        super().__init__()
        self.setupUi(self)
        self.id_cua = id_cua
        self.label_autor.setText(autor)
        self.label_titulo.setText(titulo)
        self.label_contenido.setText(contenido)
        self.controller = None
        self.init()

    def init(self):
        self.btn_agrandar.clicked.connect(self.clickAgrandar)

    def setController(self, controller):
        """Todos los Qwidets le notifican al mismo controller
        """
        self.controller = controller

    def clickAgrandar(self):
        self.controller.agrandar(self.id_cua)