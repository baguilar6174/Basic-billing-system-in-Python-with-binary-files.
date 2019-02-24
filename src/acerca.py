# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'acerca.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ventanaAcerca(object):
    def setupUi(self, ventanaAcerca):
        ventanaAcerca.setObjectName("ventanaAcerca")
        ventanaAcerca.resize(569, 377)
        ventanaAcerca.setMinimumSize(QtCore.QSize(569, 377))
        ventanaAcerca.setMaximumSize(QtCore.QSize(569, 377))
        self.label = QtWidgets.QLabel(ventanaAcerca)
        self.label.setGeometry(QtCore.QRect(20, 200, 511, 171))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("recursos/logo_principal.png"))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(ventanaAcerca)
        self.label_3.setGeometry(QtCore.QRect(40, 30, 501, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(ventanaAcerca)
        self.label_4.setGeometry(QtCore.QRect(250, 190, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(ventanaAcerca)
        self.label_5.setGeometry(QtCore.QRect(200, 160, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(ventanaAcerca)
        self.label_6.setGeometry(QtCore.QRect(180, 90, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(ventanaAcerca)
        self.label_7.setGeometry(QtCore.QRect(140, 70, 311, 181))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("recursos/logo_u (1).png"))
        self.label_7.setObjectName("label_7")
        self.label.raise_()
        self.label_7.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()

        self.retranslateUi(ventanaAcerca)
        QtCore.QMetaObject.connectSlotsByName(ventanaAcerca)

    def retranslateUi(self, ventanaAcerca):
        _translate = QtCore.QCoreApplication.translate
        ventanaAcerca.setWindowTitle(_translate("ventanaAcerca", "Acerca de ModoMueblería"))
        self.label_3.setText(_translate("ventanaAcerca", "Sistema da facturación y mantenimiento de Categorias y productos"))
        self.label_4.setText(_translate("ventanaAcerca", "Bryan Aguilar"))
        self.label_5.setText(_translate("ventanaAcerca", "Facultad de Ingeniería"))
        self.label_6.setText(_translate("ventanaAcerca", "Lenguajes de Programación"))

