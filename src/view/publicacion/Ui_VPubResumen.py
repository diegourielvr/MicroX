# Form implementation generated from reading ui file '.\src\view\publicacion\Ui_VPubResumen.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_VPubResumen(object):
    def setupUi(self, VPubResumen):
        VPubResumen.setObjectName("VPubResumen")
        VPubResumen.resize(480, 140)
        VPubResumen.setMinimumSize(QtCore.QSize(480, 0))
        VPubResumen.setMaximumSize(QtCore.QSize(480, 140))
        self.verticalLayout = QtWidgets.QVBoxLayout(VPubResumen)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=VPubResumen)
        self.frame.setMinimumSize(QtCore.QSize(0, 140))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_agrandar = QtWidgets.QPushButton(parent=self.frame_2)
        self.btn_agrandar.setStyleSheet("font: 10pt \"Inter\";")
        self.btn_agrandar.setObjectName("btn_agrandar")
        self.verticalLayout_3.addWidget(self.btn_agrandar, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(parent=self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_titulo = QtWidgets.QLabel(parent=self.frame_3)
        self.label_titulo.setStyleSheet("font: 700 10pt \"Inter\";")
        self.label_titulo.setObjectName("label_titulo")
        self.verticalLayout_4.addWidget(self.label_titulo)
        self.label_autor = QtWidgets.QLabel(parent=self.frame_3)
        self.label_autor.setStyleSheet("font: 10pt \"Inter\";")
        self.label_autor.setObjectName("label_autor")
        self.verticalLayout_4.addWidget(self.label_autor)
        self.label_contenido = QtWidgets.QLabel(parent=self.frame_3)
        self.label_contenido.setStyleSheet("font: 10pt \"Inter\";")
        self.label_contenido.setObjectName("label_contenido")
        self.verticalLayout_4.addWidget(self.label_contenido)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(VPubResumen)
        QtCore.QMetaObject.connectSlotsByName(VPubResumen)

    def retranslateUi(self, VPubResumen):
        _translate = QtCore.QCoreApplication.translate
        VPubResumen.setWindowTitle(_translate("VPubResumen", "Form"))
        self.btn_agrandar.setText(_translate("VPubResumen", "Agrandar"))
        self.label_titulo.setText(_translate("VPubResumen", "Titulo"))
        self.label_autor.setText(_translate("VPubResumen", "Autor"))
        self.label_contenido.setText(_translate("VPubResumen", "Contenido"))