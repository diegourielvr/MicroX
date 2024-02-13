from PyQt6.QtWidgets import QMainWindow, QScrollArea, QVBoxLayout, QWidget

from src.view.vMisPub.Ui_VMisPub import Ui_VMisPub


class GUI_VMisPub(QMainWindow, Ui_VMisPub):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.controller = None
        self.layout = QVBoxLayout()
        self.scroll_area = QScrollArea()
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.init()

    def init(self):
        self.btn_regresar.clicked.connect(self.clickRegresar)

        self.scroll_widget.setLayout(self.scroll_layout)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.scroll_widget)

        self.layout.addWidget(self.scroll_area)
        self.frame_publicaciones.setLayout(self.layout)

    def setController(self, controller):
        self.controller = controller

    def clickRegresar(self):
        self.controller.regresar()

    def cargarWidget(self, widget):
        self.scroll_layout.addWidget(widget)

    def limpiarWidgets(self):
        if self.scroll_layout is not None:
            while self.scroll_layout.count():
                child = self.scroll_layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
