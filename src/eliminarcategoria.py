# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EliminarCategoria.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BorrarCategoria(object):
    def setupUi(self, BorrarCategoria):
        BorrarCategoria.setObjectName("BorrarCategoria")
        BorrarCategoria.resize(595, 543)
        BorrarCategoria.setMinimumSize(QtCore.QSize(595, 543))
        BorrarCategoria.setMaximumSize(QtCore.QSize(595, 543))
        self.line_12 = QtWidgets.QFrame(BorrarCategoria)
        self.line_12.setGeometry(QtCore.QRect(10, 20, 20, 61))
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.label_30 = QtWidgets.QLabel(BorrarCategoria)
        self.label_30.setGeometry(QtCore.QRect(30, 210, 211, 21))
        self.label_30.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_30.setObjectName("label_30")
        self.tabla_categorias = QtWidgets.QTableWidget(BorrarCategoria)
        self.tabla_categorias.setGeometry(QtCore.QRect(30, 240, 241, 171))
        self.tabla_categorias.setAutoFillBackground(False)
        self.tabla_categorias.setLineWidth(1)
        self.tabla_categorias.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabla_categorias.setAlternatingRowColors(True)
        self.tabla_categorias.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tabla_categorias.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabla_categorias.setShowGrid(True)
        self.tabla_categorias.setGridStyle(QtCore.Qt.DashLine)
        self.tabla_categorias.setRowCount(10)
        self.tabla_categorias.setColumnCount(2)
        self.tabla_categorias.setObjectName("tabla_categorias")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla_categorias.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla_categorias.setHorizontalHeaderItem(1, item)
        self.tabla_categorias.horizontalHeader().setDefaultSectionSize(100)
        self.line_8 = QtWidgets.QFrame(BorrarCategoria)
        self.line_8.setGeometry(QtCore.QRect(20, 180, 551, 21))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.label_31 = QtWidgets.QLabel(BorrarCategoria)
        self.label_31.setGeometry(QtCore.QRect(300, 240, 181, 21))
        self.label_31.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_31.setObjectName("label_31")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(BorrarCategoria)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(400, 460, 167, 70))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.boton_eliminar_categoria = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.boton_eliminar_categoria.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("recursos/borrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_eliminar_categoria.setIcon(icon)
        self.boton_eliminar_categoria.setIconSize(QtCore.QSize(70, 60))
        self.boton_eliminar_categoria.setObjectName("boton_eliminar_categoria")
        self.horizontalLayout_17.addWidget(self.boton_eliminar_categoria)
        self.boton_cancelar_categoria = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.boton_cancelar_categoria.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("recursos/cancelar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_cancelar_categoria.setIcon(icon1)
        self.boton_cancelar_categoria.setIconSize(QtCore.QSize(65, 60))
        self.boton_cancelar_categoria.setObjectName("boton_cancelar_categoria")
        self.horizontalLayout_17.addWidget(self.boton_cancelar_categoria)
        self.line_10 = QtWidgets.QFrame(BorrarCategoria)
        self.line_10.setGeometry(QtCore.QRect(20, 430, 551, 21))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(BorrarCategoria)
        self.line_11.setGeometry(QtCore.QRect(560, 80, 20, 101))
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.text_nombre_categoria = QtWidgets.QLabel(BorrarCategoria)
        self.text_nombre_categoria.setGeometry(QtCore.QRect(390, 280, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.text_nombre_categoria.setFont(font)
        self.text_nombre_categoria.setObjectName("text_nombre_categoria")
        self.line_4 = QtWidgets.QFrame(BorrarCategoria)
        self.line_4.setGeometry(QtCore.QRect(560, 190, 20, 251))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_9 = QtWidgets.QFrame(BorrarCategoria)
        self.line_9.setGeometry(QtCore.QRect(20, 10, 551, 21))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_14 = QtWidgets.QFrame(BorrarCategoria)
        self.line_14.setGeometry(QtCore.QRect(280, 190, 20, 251))
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.line_6 = QtWidgets.QFrame(BorrarCategoria)
        self.line_6.setGeometry(QtCore.QRect(20, 70, 551, 21))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.label_28 = QtWidgets.QLabel(BorrarCategoria)
        self.label_28.setGeometry(QtCore.QRect(510, 0, 101, 101))
        self.label_28.setText("")
        self.label_28.setPixmap(QtGui.QPixmap("recursos/iconoadministrar.png"))
        self.label_28.setObjectName("label_28")
        self.label_3 = QtWidgets.QLabel(BorrarCategoria)
        self.label_3.setGeometry(QtCore.QRect(170, 30, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.line_3 = QtWidgets.QFrame(BorrarCategoria)
        self.line_3.setGeometry(QtCore.QRect(10, 190, 20, 251))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(BorrarCategoria)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 90, 491, 84))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("recursos/logo.png"))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_13 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_6.addWidget(self.label_13, QtCore.Qt.AlignHCenter)
        self.label_14 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_14.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_6.addWidget(self.label_14, QtCore.Qt.AlignHCenter)
        self.label_15 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_6.addWidget(self.label_15, QtCore.Qt.AlignHCenter)
        self.label_18 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_18.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_6.addWidget(self.label_18)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        self.line_7 = QtWidgets.QFrame(BorrarCategoria)
        self.line_7.setGeometry(QtCore.QRect(20, 170, 551, 21))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_5 = QtWidgets.QFrame(BorrarCategoria)
        self.line_5.setGeometry(QtCore.QRect(10, 80, 20, 101))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_13 = QtWidgets.QFrame(BorrarCategoria)
        self.line_13.setGeometry(QtCore.QRect(560, 20, 20, 61))
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.label_33 = QtWidgets.QLabel(BorrarCategoria)
        self.label_33.setGeometry(QtCore.QRect(300, 330, 201, 21))
        self.label_33.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_33.setObjectName("label_33")
        self.text_codigo_eliminar = QtWidgets.QLabel(BorrarCategoria)
        self.text_codigo_eliminar.setGeometry(QtCore.QRect(390, 380, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.text_codigo_eliminar.setFont(font)
        self.text_codigo_eliminar.setObjectName("text_codigo_eliminar")
        self.botonSeleccionar = QtWidgets.QPushButton(BorrarCategoria)
        self.botonSeleccionar.setGeometry(QtCore.QRect(120, 460, 67, 71))
        self.botonSeleccionar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("recursos/1-Touch-with-pressure-of-one-finger-of-the-hand-on-a-circular-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botonSeleccionar.setIcon(icon2)
        self.botonSeleccionar.setIconSize(QtCore.QSize(40, 60))
        self.botonSeleccionar.setObjectName("botonSeleccionar")

        self.retranslateUi(BorrarCategoria)
        QtCore.QMetaObject.connectSlotsByName(BorrarCategoria)

    def retranslateUi(self, BorrarCategoria):
        _translate = QtCore.QCoreApplication.translate
        BorrarCategoria.setWindowTitle(_translate("BorrarCategoria", "Eliminar Categoría"))
        self.label_30.setText(_translate("BorrarCategoria", "Selecciona la categoría que deseas eliminar"))
        item = self.tabla_categorias.horizontalHeaderItem(0)
        item.setText(_translate("BorrarCategoria", "Categoría"))
        item = self.tabla_categorias.horizontalHeaderItem(1)
        item.setText(_translate("BorrarCategoria", "Código"))
        self.label_31.setText(_translate("BorrarCategoria", "La categoría seleccionada es.:"))
        self.boton_eliminar_categoria.setToolTip(_translate("BorrarCategoria", "Eliminar categoriá"))
        self.boton_cancelar_categoria.setToolTip(_translate("BorrarCategoria", "Cancelar"))
        self.text_nombre_categoria.setText(_translate("BorrarCategoria", "\"Categoría Seleccionada\""))
        self.label_3.setText(_translate("BorrarCategoria", "Borrado de Categoría"))
        self.label_13.setText(_translate("BorrarCategoria", "MODO MUEBLERÍA COMPAÑÍA LTDA"))
        self.label_14.setText(_translate("BorrarCategoria", "Av. 12 de Abril y Av. Loja"))
        self.label_15.setText(_translate("BorrarCategoria", "Cuenca - Ecuador"))
        self.label_18.setText(_translate("BorrarCategoria", "Telf: 0991538711"))
        self.label_33.setText(_translate("BorrarCategoria", "El código de la categoría selecionada es.:"))
        self.text_codigo_eliminar.setText(_translate("BorrarCategoria", "\"Codigo Categoría\""))
        self.botonSeleccionar.setToolTip(_translate("BorrarCategoria", "Seleccionar producto para eliminar"))

