# Form implementation generated from reading ui file '.\src\view\vPubDetalle\Ui_VPubDetalle.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_VPubDetalle(object):
    def setupUi(self, VPubDetalle):
        VPubDetalle.setObjectName("VPubDetalle")
        VPubDetalle.resize(500, 327)
        VPubDetalle.setMinimumSize(QtCore.QSize(500, 0))
        VPubDetalle.setMaximumSize(QtCore.QSize(500, 500))
        self.centralwidget = QtWidgets.QWidget(parent=VPubDetalle)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(parent=self.frame)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.frame_4)
        self.label.setStyleSheet("font: 700 20pt \"Inter\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(parent=self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(parent=self.frame_3)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 70))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 128))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_avatar = QtWidgets.QLabel(parent=self.frame_2)
        self.label_avatar.setMinimumSize(QtCore.QSize(64, 64))
        self.label_avatar.setObjectName("label_avatar")
        self.horizontalLayout_4.addWidget(self.label_avatar, 0, QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_autor = QtWidgets.QLabel(parent=self.frame_2)
        self.label_autor.setStyleSheet("font: 700 14pt \"Inter\";")
        self.label_autor.setObjectName("label_autor")
        self.horizontalLayout_4.addWidget(self.label_autor)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.label_titulo = QtWidgets.QLabel(parent=self.frame_3)
        self.label_titulo.setStyleSheet("font: 12pt \"Inter\";")
        self.label_titulo.setObjectName("label_titulo")
        self.verticalLayout_3.addWidget(self.label_titulo)
        self.frame_5 = QtWidgets.QFrame(parent=self.frame_3)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_fecha_modificacion = QtWidgets.QLabel(parent=self.frame_5)
        self.label_fecha_modificacion.setStyleSheet("font: 10pt \"Inter\";")
        self.label_fecha_modificacion.setObjectName("label_fecha_modificacion")
        self.horizontalLayout_2.addWidget(self.label_fecha_modificacion, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.textArea_contenido = QtWidgets.QTextEdit(parent=self.frame_3)
        self.textArea_contenido.setEnabled(True)
        self.textArea_contenido.setMaximumSize(QtCore.QSize(16777215, 100))
        self.textArea_contenido.setStyleSheet("font: 10pt \"Inter\";")
        self.textArea_contenido.setReadOnly(True)
        self.textArea_contenido.setObjectName("textArea_contenido")
        self.verticalLayout_3.addWidget(self.textArea_contenido)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_imagen = QtWidgets.QFrame(parent=self.frame)
        self.frame_imagen.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_imagen.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_imagen.setObjectName("frame_imagen")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_imagen)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_imagen = QtWidgets.QLabel(parent=self.frame_imagen)
        self.label_imagen.setMinimumSize(QtCore.QSize(0, 0))
        self.label_imagen.setText("")
        self.label_imagen.setObjectName("label_imagen")
        self.horizontalLayout_3.addWidget(self.label_imagen, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout_2.addWidget(self.frame_imagen)
        self.verticalLayout.addWidget(self.frame)
        VPubDetalle.setCentralWidget(self.centralwidget)

        self.retranslateUi(VPubDetalle)
        QtCore.QMetaObject.connectSlotsByName(VPubDetalle)

    def retranslateUi(self, VPubDetalle):
        _translate = QtCore.QCoreApplication.translate
        VPubDetalle.setWindowTitle(_translate("VPubDetalle", "MainWindow"))
        self.label.setText(_translate("VPubDetalle", "VPub Detalle"))
        self.label_avatar.setText(_translate("VPubDetalle", "img"))
        self.label_autor.setText(_translate("VPubDetalle", "Autor"))
        self.label_titulo.setText(_translate("VPubDetalle", "Titulo"))
        self.label_fecha_modificacion.setText(_translate("VPubDetalle", "Fecha"))
        self.textArea_contenido.setPlaceholderText(_translate("VPubDetalle", "Contenio..."))
