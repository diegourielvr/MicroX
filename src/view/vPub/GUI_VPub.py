from PyQt6.QtWidgets import QMainWindow, QScrollArea, QWidget, QVBoxLayout, QPushButton

from src.view.vPub.Ui_VPub import Ui_VPub


class GUI_VPub(QMainWindow, Ui_VPub):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.controller = None
        self.layout = QVBoxLayout() # Layout para el frame_publicaciones
        self.scroll_area = QScrollArea() # Area que permite hacer scroll
        self.scroll_widget = QWidget() # Widget que va dentro de scroll_area y recibe widgets vpubresumen
        # Para meter widgets dentro de otro widget, necesitamos un layout
        self.scroll_layout = QVBoxLayout(self.scroll_widget) # indicamos el padre del scroll_layout
        self.init()

    def init(self):
        self.btn_publicar.clicked.connect(self.clickPublicar)
        self.btn_mostrar.clicked.connect(self.clickMostrar)

        # Al widget que le quieres aplicar un layout, lo metes en su constructor
        self.scroll_widget.setLayout(self.scroll_layout) # Asignamos el layout al padre
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.scroll_widget)

        # Agregar un layout al frame_publicaciones para poder agregar un widget scrollarea
        self.layout.addWidget(self.scroll_area)
        self.frame_publicaciones.setLayout(self.layout)

    def setController(self, controller):
        self.controller = controller

    def clickPublicar(self):
        self.controller.publicar()

    def clickMostrar(self):
        self.controller.mostrarMisPublicaciones()

    def cargarWidget(self, widget):
        self.scroll_layout.addWidget(widget)

    def limpiarWidgets(self):
        if self.scroll_layout is not None:
            while self.scroll_layout.count():
                child = self.scroll_layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
