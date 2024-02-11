import os.path

from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import QSize
from src.view.registrarse.avatar.Ui_Avatar import Ui_Avatar


class GUI_Avatar(QMainWindow, Ui_Avatar):
    def __init__(self, padre=None):
        super().__init__()
        self.setupUi(self)
        self.controller = None
        self.path_avatars_default= "src\\static\\avatars\\default"
        self.file_names = ["img1.png", "img2.png", "img3.png"]
        self.init()

    def init(self):
        self.btn_quitarimagen.setVisible(False)
        self.cargarImagenes()

        self.btn_guardar.clicked.connect(self.clickGuardar)
        self.btn_subir_imagen.clicked.connect(self.clickSubirImagen)
        self.btn_quitarimagen.clicked.connect(self.clickQuitarImagen)

        self.op1.clicked.connect(self.clickImg1)
        self.op2.clicked.connect(self.clickImg2)
        self.op3.clicked.connect(self.clickImg3)

    def setController(self, controller):
        self.controller = controller

    def clickGuardar(self):
        self.controller.guardar()

    def clickSubirImagen(self):
        self.controller.subirImagen()

    def clickQuitarImagen(self):
        self.controller.quitarImagen()

    def clickImg1(self):
        cwd = os.getcwd()
        path = os.path.join(cwd, self.path_avatars_default, self.file_names[0])
        self.controller.seleccionarImagen(path)

    def clickImg2(self):
        cwd = os.getcwd()
        path = os.path.join(cwd, self.path_avatars_default, self.file_names[1])
        self.controller.seleccionarImagen(path)

    def clickImg3(self):
        cwd = os.getcwd()
        path = os.path.join(cwd, self.path_avatars_default, self.file_names[2])
        self.controller.seleccionarImagen(path)

    def cargarImagenes(self):
        cwd = os.getcwd()
        file_path = os.path.join(cwd, self.path_avatars_default, self.file_names[0])
        icon = QIcon(file_path)
        self.op1.setIcon(icon)
        file_path = os.path.join(cwd, self.path_avatars_default, self.file_names[1])
        icon = QIcon(file_path)
        self.op2.setIcon(icon)
        file_path = os.path.join(cwd, self.path_avatars_default, self.file_names[2])
        icon = QIcon(file_path)
        self.op3.setIcon(icon)


    def cargarImagen(self, pixmap):
        """Cargar un pixmap cargado en un label
        """
        #self.frame_avatar.layout().addWidget(label)
        self.label_avatar.setPixmap(pixmap)
        self.btn_quitarimagen.setVisible(True)

    def limpiarImagen(self):
        self.label_avatar.clear()
        self.btn_quitarimagen.setVisible(False)
