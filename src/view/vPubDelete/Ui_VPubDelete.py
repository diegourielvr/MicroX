# Form implementation generated from reading ui file '.\src\view\vPubDelete\Ui_VPubDelete.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_VPubDelete(object):
    def setupUi(self, VPubDelete):
        VPubDelete.setObjectName("VPubDelete")
        VPubDelete.resize(300, 200)
        VPubDelete.setMinimumSize(QtCore.QSize(300, 200))
        VPubDelete.setMaximumSize(QtCore.QSize(300, 200))
        self.centralwidget = QtWidgets.QWidget(parent=VPubDelete)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setStyleSheet("font: 700 10pt \"Inter\";")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_cancelar = QtWidgets.QPushButton(parent=self.frame_2)
        self.btn_cancelar.setStyleSheet("font: 10pt \"Inter\";")
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.horizontalLayout.addWidget(self.btn_cancelar)
        self.btn_eliminar = QtWidgets.QPushButton(parent=self.frame_2)
        self.btn_eliminar.setStyleSheet("font: 10pt \"Inter\";")
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.horizontalLayout.addWidget(self.btn_eliminar)
        self.verticalLayout.addWidget(self.frame_2)
        VPubDelete.setCentralWidget(self.centralwidget)

        self.retranslateUi(VPubDelete)
        QtCore.QMetaObject.connectSlotsByName(VPubDelete)

    def retranslateUi(self, VPubDelete):
        _translate = QtCore.QCoreApplication.translate
        VPubDelete.setWindowTitle(_translate("VPubDelete", "MainWindow"))
        self.label.setText(_translate("VPubDelete", "¿Deseas eliminar la publicación?"))
        self.btn_cancelar.setText(_translate("VPubDelete", "Cancelar"))
        self.btn_eliminar.setText(_translate("VPubDelete", "Eliminar"))