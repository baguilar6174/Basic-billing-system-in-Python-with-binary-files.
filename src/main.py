import sys
import pickle
import re
import random

from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import QTableWidgetItem,QTableWidgetItem,QMessageBox,QInputDialog,QLineEdit
from principal import Ui_MainWindow
from informacionproductos import Ui_InformacionProductos
from realizarpedido import Ui_RealizarPedido
from eliminarcategoria import Ui_BorrarCategoria
from modificarcategoria import Ui_ModificarCategoria
from categoriaregistro import Ui_RegistroCategoria
from eliminarproducto import Ui_BorrarProducto
from modificarproducto import Ui_ModificarProducto
from productoregistro import Ui_IngresoProducto
from facturacliente import Ui_Factura
from datoscliente import Ui_RegistroDatosPersonales
from informacionventas import Ui_infoventas
from acerca import Ui_ventanaAcerca

class ModoMuebleria():
    def __init__(self):
        
        self.productos_por_categoria = []
        self.suma = random.randint(1,1000)
        
        try:
            with open("productos.dat","rb") as f:
                self.productos = pickle.load(f)
            f.close()
        except:
            self.productos = []
                
        try:
            with open("categorias.dat","rb") as g:
                self.categorias = pickle.load(g)
            g.close()
        except:
            self.categorias = []
            
        try:
            with open("facturas.dat","rb") as h:
                self.pedidos_consumidor_final = pickle.load(h)
            h.close()
        except:
            self.pedidos_consumidor_final = []
        
        try:
            with open("recursos/fechasCf.dat","rb") as i:
                self.fechas_consumidor_final = pickle.load(i)
            i.close()
        except:
            self.fechas_consumidor_final = []
        
        try:
            with open("recursos/datosCliente.dat","rb") as i:
                self.datos_cliente = pickle.load(i)
            i.close()
        except:
            self.datos_cliente = []
        
    def tamano_productos(self):
        return len(self.productos)
    
    def tamano_categorias(self):
        return len(self.categorias)
    
    def tamano_pedidos_consumidor_final(self):
        return len(self.pedidos_consumidor_final)
        
    def tamano_fechas_consumidor_final(self):
        return len(self.fechas_consumidor_final)
        
    def tamano_datos_cliente(self):
        return len(self.datos_cliente)
    
    def agregar_categoria(self, nombre, codigo, descripcion):
        self.categorias.append(nombre+"$"+codigo+"$"+descripcion)
        with open("categorias.dat","wb") as f:
            pickle.dump(self.categorias,f,pickle.HIGHEST_PROTOCOL)
        f.close()
        print("Categoria agregada!!")
    
    def agregar_producto(self, categoria, precio, codigo, nombre,descripcion):
        self.productos.append(categoria+"$"+precio+"$"+codigo+"$"+nombre+"$"+descripcion)
        with open("productos.dat","wb") as f:
            pickle.dump(self.productos,f,pickle.HIGHEST_PROTOCOL)
        f.close()
        print("Producto agregado!!")
    
    def mostrar_categorias(self):
        for elemento in self.categorias:
            arreglo = elemento.split("$")
            print("Nombre Categoria      : " + arreglo[0])
            print("Codigo Categoria      : " + arreglo[1])
            print("Descripcion Categoria : " + arreglo[2])
            print("\n")
    
    def mostrar_productos(self):
        for elemento in self.productos:
            arreglo = elemento.split("$")
            print("Categoria Producto   : " + arreglo[0])
            print("Precio Producto      : " + arreglo[1])
            print("Codigo Producto      : " + arreglo[2])
            print("Nombre Producto      : " + arreglo[3])
            print("Descripcion Producto : " + arreglo[4])
            print("\n")
    
    def mostrar_pedidos_consumidor_final(self):
        for elemento in self.pedidos_consumidor_final:
            arreglo = elemento.split("$")
            print("Categoria : " + arreglo[0])
            print("Codigo    : " + arreglo[1])
            print("Producto  : " + arreglo[2])
            print("Precio    : " + arreglo[3])
            print("Cantidad  : " + arreglo[4])
            print("Clave     : " + arreglo[5])
            print("\n")
    
    def mostrar_fechas_consumidor_final(self):
        for elemento in self.fechas_consumidor_final:
            arreglo = elemento.split("$")
            print("Fecha  : " + arreglo[0])
            print("Clave  : " + arreglo[1])
            print("\n")
        
    def mostrar_datos_cliente(self):
        for elemento in self.datos_cliente:
            arreglo = elemento.split("$")
            print("Nombre     : " + arreglo[0])
            print("Fecha      : " + arreglo[1])
            print("Direccion  : " + arreglo[2])
            print("Cedula     : " + arreglo[3])
            print("Telefono   : " + arreglo[4])
            print("Clave      : " + arreglo[5])
            print("\n")
            
    def recuperar_lista_productos(self):
        return self.productos
    
    def recuperar_lista_categorias(self):
        return self.categorias
    
    def recuperar_lista_pedidos_consumidor_final(self):
        return self.pedidos_consumidor_final
    
    def recuperar_lista_fechas_consumidor_final(self):
        return self.fechas_consumidor_final
    
    def recuperar_lista_datos_cliente(self):
        return self.datos_cliente
    
    def nombres_Categorias(self):
        nuevo = []
        for elemento in self.categorias:
            arreglo = elemento.split("$")
            nuevo.append(arreglo[0])
        return nuevo
    
    def fechas_ventas_consumidor_final(self):
        nuevo = []
        for elemento in self.fechas_consumidor_final:
            arreglo = elemento.split("$")
            nuevo.append(arreglo[0])
        return nuevo
    
    def fechas_ventas_cliente(self):
        nuevo = []
        for elemento in self.datos_cliente:
            arreglo = elemento.split("$")
            nuevo.append(arreglo[1])
        return nuevo
    
    def recuperar_productos_categoria(self,categoria):
        self.productos_por_categoria.clear()
        for elemento in self.productos:
            arreglo = elemento.split("$")
            if(categoria == arreglo[0]):
                self.productos_por_categoria.append(arreglo[0]+"$"+arreglo[1]+"$"+arreglo[2]+"$"+arreglo[3]+"$"+arreglo[4])
        
        return self.productos_por_categoria
    
    def tamano_productos_por_categoria(self):
        return len(self.productos_por_categoria)
    
    def modificar_categoria(self,original,nombre,codigo,descripcion):
        
        Noencontrado = True;
        for i in range(len(self.categorias)):
            lista_indi = str(self.categorias[i]).split("$")
            if codigo == lista_indi[1]:
                lista_indi[0] = nombre
                lista_indi[2] = descripcion
                self.categorias.pop(i)
                self.categorias.insert(i,(lista_indi[0]+"$"+codigo+"$"+lista_indi[2]))
                with open("categorias.dat","wb") as f:
                    pickle.dump(self.categorias,f,pickle.HIGHEST_PROTOCOL)
                f.close()
                Noencontrado = False
                break
                
        if Noencontrado == True:
            print("Contacto no encontrado")
            
        self.modificar_categoria_lista_productos(original,nombre)
    
    def modificar_categoria_lista_productos(self,original,nombre):
        
        for i in range(len(self.productos)):
            lista_indi = str(self.productos[i]).split("$")
            if original == lista_indi[0]:
                lista_indi[0] = nombre
                self.productos.pop(i)
                self.productos.insert(i,(lista_indi[0]+"$"+lista_indi[1]+"$"+lista_indi[2]+"$"+lista_indi[3]+"$"+lista_indi[4]))
                with open("productos.dat","wb") as f:
                    pickle.dump(self.productos,f,pickle.HIGHEST_PROTOCOL)
                f.close()
                
    def modificar_producto(self,nombre,codigo,descripcion,precio):
        
        for i in range(len(self.productos)):
            lista_indi = str(self.productos[i]).split("$")
            if codigo == lista_indi[2]:
                lista_indi[1] = precio
                lista_indi[3] = nombre
                lista_indi[4] = descripcion
                self.productos.pop(i)
                self.productos.insert(i,(lista_indi[0]+"$"+lista_indi[1]+"$"+codigo+"$"+lista_indi[3]+"$"+lista_indi[4]))
                with open("productos.dat","wb") as f:
                    pickle.dump(self.productos,f,pickle.HIGHEST_PROTOCOL)
                f.close()
                break
    
    def eliminar_producto(self,codigo):    
        for i in range(len(self.productos)):
            lista_indi = str(self.productos[i]).split("$")
            if codigo == lista_indi[2]:
                self.productos.pop(i)
                with open("productos.dat","wb") as f:
                    pickle.dump(self.productos,f,pickle.HIGHEST_PROTOCOL)
                f.close()
                break
    
    def eliminar_categoria(self,codigo):
        
        Noencontrado = True;
        for i in range(len(self.categorias)):
            lista_indi = str(self.categorias[i]).split("$")
            if codigo == lista_indi[1]:
                self.categorias.pop(i)
                with open("categorias.dat","wb") as f:
                    pickle.dump(self.categorias,f,pickle.HIGHEST_PROTOCOL)
                f.close()
                Noencontrado = False
                break
                
        if Noencontrado == True:
            print("Contacto no encontrado")
            
    def agregar_pedido_consumidor_final(self,categoria,codigo,producto,precio,cantidad,clave):
        self.pedidos_consumidor_final.append(categoria+"$"+codigo+"$"+producto+"$"+precio+"$"+cantidad+"$"+clave)
        with open("facturas.dat","wb") as f:
            pickle.dump(self.pedidos_consumidor_final,f,pickle.HIGHEST_PROTOCOL)
        f.close()
        print("Pedido agregado!!")
    
    def agregar_fecha_consumidor_final(self,fecha,clave):
        self.suma += self.tamano_pedidos_consumidor_final()
        self.fechas_consumidor_final.append(fecha+"$"+clave)
        with open("recursos/fechasCF.dat","wb") as f:
            pickle.dump(self.fechas_consumidor_final,f,pickle.HIGHEST_PROTOCOL)
        f.close()
        print("Fecha agregado!!")
    
    def getClave(self):
        return self.suma
    
    def agregar_cliente(self,nombre,fecha,direccion,cedula,telefono,clave):
        self.suma += self.tamano_pedidos_consumidor_final()
        self.datos_cliente.append(nombre+"$"+fecha+"$"+direccion+"$"+cedula+"$"+telefono+"$"+clave)
        with open("recursos/datosCliente.dat","wb") as f:
            pickle.dump(self.datos_cliente,f,pickle.HIGHEST_PROTOCOL)
        f.close()
        print("Cliente agregado!!")
        
    def recuperar_clave_producto(self,categoria):
        nuevo = []
        for i in range(len(self.pedidos_consumidor_final)):
            lista_indi = str(self.pedidos_consumidor_final[i]).split("$")
            if categoria == lista_indi[0]:
                nuevo.append(lista_indi[1]+"$"+lista_indi[2]+"$"+lista_indi[3]+"$"+lista_indi[4]+"$"+lista_indi[5])
        return nuevo
    
    def recuperar_clave_consumidor_final(self,fecha):
        nuevo = []
        for i in range(len(self.fechas_consumidor_final)):
            lista_indi = str(self.fechas_consumidor_final[i]).split("$")
            if fecha == lista_indi[0]:
                nuevo.append("Consumidor Final"+"$"+lista_indi[0]+"$"+lista_indi[1])
        return nuevo
    
    def recuperar_clave_cliente(self,fecha):
        nuevo = []
        for i in range(len(self.datos_cliente)):
            lista_indi = str(self.datos_cliente[i]).split("$")
            if fecha == lista_indi[1]:
                nuevo.append(lista_indi[0]+"$"+lista_indi[1]+"$"+lista_indi[5])
        return nuevo
    
    def recuperar_clave_fecha(self,lista):
        for i in range(len(lista)):
            lista_indi = str(lista[i]).split("$")
            return lista_indi[2]
        
        
""" Abstraccion de la clase Modo Muebleria"""

empresa = ModoMuebleria()

""" ------------------------------------- """

class VerProductos(QtWidgets.QWidget,Ui_InformacionProductos):
    def __init__(self,parent=None):
        super(VerProductos,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.salir)
        self.mostrar_productos()
        self.comboBox_categorias_informacion.addItems(empresa.nombres_Categorias())
        self.comboBox_categorias_informacion.currentTextChanged.connect(self.cambiar_categoria)
    
    def cambiar_categoria(self):
        categoria = self.comboBox_categorias_informacion.currentText()
        if(categoria == "Todas"):
            self.tabla_productos_informacion.clearContents()
            self.mostrar_productos()
        else:
            self.tabla_productos_informacion.clearContents()
            tam = empresa.tamano_productos()
            i=0
            j=0
            lista_nueva = empresa.recuperar_lista_productos()
            while i < tam :
                lista_indi = str(lista_nueva[i]).split("$")
                if(categoria == lista_indi[0]):
                    self.tabla_productos_informacion.setItem(j, 0, QTableWidgetItem(str(lista_indi[0])))
                    self.tabla_productos_informacion.setItem(j, 1, QTableWidgetItem(str(lista_indi[1])))
                    self.tabla_productos_informacion.setItem(j, 2, QTableWidgetItem(str(lista_indi[2])))
                    self.tabla_productos_informacion.setItem(j, 3, QTableWidgetItem(str(lista_indi[3])))
                    self.tabla_productos_informacion.setItem(j, 4, QTableWidgetItem(str(lista_indi[4])))
                    j = j+1
                i = i+1
                
    def mostrar_productos(self):
        tam = empresa.tamano_productos()
        i=0
        lista_nueva = empresa.recuperar_lista_productos()
        while i < tam :
            lista_indi = str(lista_nueva[i]).split("$")
            self.tabla_productos_informacion.setItem(i, 0, QTableWidgetItem(str(lista_indi[0])))
            self.tabla_productos_informacion.setItem(i, 1, QTableWidgetItem(str(lista_indi[1])))
            self.tabla_productos_informacion.setItem(i, 2, QTableWidgetItem(str(lista_indi[2])))
            self.tabla_productos_informacion.setItem(i, 3, QTableWidgetItem(str(lista_indi[3])))
            self.tabla_productos_informacion.setItem(i, 4, QTableWidgetItem(str(lista_indi[4])))
            i = i+1
        
    def salir(self):
        self.close()

class Datos_Cliente(QtWidgets.QWidget,Ui_RegistroDatosPersonales):
    def __init__(self,parent=None):
        super(Datos_Cliente,self).__init__(parent)
        self.setupUi(self)
        self.clave = empresa.getClave()
        self.boton_Siguiente_Datos.clicked.connect(self.guardar_datos)
        self.boton_Cancelar_Datos.clicked.connect(self.salir)
        self.text_numero_factura_datos.setText(str(self.clave))
        
    def guardar_datos(self):
        
        nombre = self.edit_cliente.text()
        fecha = self.edit_fecha.text()
        direccion = self.edit_direccion.text()
        cedula = self.edit_cedula.text()
        telefono = self.edit_telefono.text()
        
        empresa.agregar_cliente(nombre,fecha,direccion,cedula,telefono,str(self.clave))
        empresa.mostrar_datos_cliente()
        
        self.close()
        self.ventana_Factura = Factura("Cliente")
        self.ventana_Factura.show()
        
        self.edit_cliente.clear()
        self.edit_fecha.clear()
        self.edit_direccion.clear()
        self.edit_cedula.clear()
        self.edit_telefono.clear()
        
    def salir(self):
        self.close()

class HacerPedido(QtWidgets.QWidget,Ui_RealizarPedido):
    def __init__(self,parent=None):
        super(HacerPedido,self).__init__(parent)
        self.setupUi(self)
        self.mostrar_productos()
        self.clave = empresa.getClave()
        self.comboBox_categorias_pedido.addItems(empresa.nombres_Categorias())
        self.comboBox_categorias_pedido.currentTextChanged.connect(self.cambiar_categoria)
        self.boton_agregar.clicked.connect(self.seleccionar_Fila)
        self.boton_atras_pedido.clicked.connect(self.salir)
        self.boton_aceptar_pedido.setEnabled(False)
        self.boton_aceptar_pedido.clicked.connect(self.llenar_Datos)
    
    def cambiar_categoria(self):
        categoria = self.comboBox_categorias_pedido.currentText()
        if(categoria == "Todas"):
            self.tabla_productos_pedido.clearContents()
            self.mostrar_productos()
        else:
            self.tabla_productos_pedido.clearContents()
            tam = empresa.tamano_productos()
            i=0
            j=0
            lista_nueva = empresa.recuperar_lista_productos()
            while i < tam :
                lista_indi = str(lista_nueva[i]).split("$")
                if(categoria == lista_indi[0]):
                    self.tabla_productos_pedido.setItem(j, 0, QTableWidgetItem(str(lista_indi[0])))
                    self.tabla_productos_pedido.setItem(j, 1, QTableWidgetItem(str(lista_indi[1])))
                    self.tabla_productos_pedido.setItem(j, 2, QTableWidgetItem(str(lista_indi[2])))
                    self.tabla_productos_pedido.setItem(j, 3, QTableWidgetItem(str(lista_indi[3])))
                    self.tabla_productos_pedido.setItem(j, 4, QTableWidgetItem(str(lista_indi[4])))
                    j = j+1
                i = i+1
        
    def mostrar_productos(self):
        tam = empresa.tamano_productos()
        i=0
        lista_nueva = empresa.recuperar_lista_productos()
        while i < tam :
            lista_indi = str(lista_nueva[i]).split("$")
            self.tabla_productos_pedido.setItem(i, 0, QTableWidgetItem(str(lista_indi[0])))
            self.tabla_productos_pedido.setItem(i, 1, QTableWidgetItem(str(lista_indi[1])))
            self.tabla_productos_pedido.setItem(i, 2, QTableWidgetItem(str(lista_indi[2])))
            self.tabla_productos_pedido.setItem(i, 3, QTableWidgetItem(str(lista_indi[3])))
            self.tabla_productos_pedido.setItem(i, 4, QTableWidgetItem(str(lista_indi[4])))
            i = i+1
        
    def seleccionar_Fila(self):
        value, ok = QInputDialog.getText(self, "Cantidad de productos", "Ingrese cuantos productos desea:                        ",QLineEdit.Normal, "1")
        categoria = self.comboBox_categorias_pedido.currentText()
        fila =  self.tabla_productos_pedido.currentRow()
        if(categoria == "Todas"):
            lista_nueva = empresa.recuperar_lista_productos()
            tam = empresa.tamano_productos()
            i=0
            while i < tam:
                lista_indi = str(lista_nueva[i]).split("$")
                if(i == fila):
                    empresa.agregar_pedido_consumidor_final(lista_indi[0],lista_indi[2],lista_indi[3],lista_indi[1],value,str(self.clave))
                    empresa.mostrar_pedidos_consumidor_final()
                    QMessageBox.information(self, "Agregar Producto", "Se ha agregado el producto :"+lista_indi[3],QMessageBox.Ok, QMessageBox.Ok)
                    self.boton_aceptar_pedido.setEnabled(True)
                i = i+1
        else:
            lista_nueva_2 = empresa.recuperar_productos_categoria(categoria)
            tam = empresa.tamano_productos_por_categoria()
            i=0
            while i < tam:
                lista_indi_2 = str(lista_nueva_2[i]).split("$")
                if(i == fila):
                    empresa.agregar_pedido_consumidor_final(lista_indi_2[0],lista_indi_2[2],lista_indi_2[3],lista_indi_2[1],value,str(self.clave))
                    empresa.mostrar_pedidos_consumidor_final()
                    QMessageBox.information(self, "Agregar Producto", "Se ha agregado el producto :"+lista_indi_2[3],QMessageBox.Ok, QMessageBox.Ok)
                    self.boton_aceptar_pedido.setEnabled(True)
                i = i+1
    
    def llenar_Datos(self):
        
        resultado = QMessageBox.question(self, " Tipo de factura ", "¿ Desea su factura con datos ? ", QMessageBox.Yes | QMessageBox.No)
        if (resultado == QMessageBox.Yes):
            self.close()
            self.ventana_Datos = Datos_Cliente()
            self.ventana_Datos.show()
        else:
            self.close()
            fecha, okPressed = QInputDialog.getText(self, "Fecha de emision ","Ingrese la fecha (dd/mm/yy):                          ")
            if okPressed and fecha != "":
                empresa.agregar_fecha_consumidor_final(fecha,str(self.clave))
                empresa.mostrar_fechas_consumidor_final()
                self.ventana_Factura = Factura("Consumidor Final")
                self.ventana_Factura.show()    
        
    #def generar_numero_factura(self):

    """def validar_entero(self):
        cantidad = self.edit_cantidad.text()
        validar = re.match('^[0-9]+$|^[0-9]+[.][0-9]{2}$',cantidad,re.I)
        if not validar:
            self.edit_cantidad.setStyleSheet("border: 1px solid red")
            return False
        else:
            self.edit_cantidad.setStyleSheet("border: 1px solid green")
            return True"""
    
    def salir(self):
        self.close()
    
class Factura(QtWidgets.QWidget,Ui_Factura):
    def __init__(self,tipo,parent=None):
        super(Factura,self).__init__(parent)
        self.setupUi(self)
        self.tipo = tipo
        self.pushButton.clicked.connect(self.salir)
        self.mostrar_productos()
    
    def salir(self):
        self.close()
    
    def mostrar_productos(self):
        
        fecha = ""
        num_factura = ""
        nombre = ""
        direccion = ""
        telefono = ""
        cedula = ""
        
        if(self.tipo == "Consumidor Final"):
            
            tam_fechas = empresa.tamano_fechas_consumidor_final()
            j=0
            lista_nueva_fechas = empresa.recuperar_lista_fechas_consumidor_final()
            while j < tam_fechas :
                lista_indi_fechas = str(lista_nueva_fechas[j]).split("$")
                fecha = lista_indi_fechas[0]
                num_factura = lista_indi_fechas[1]
                j = j+1

            self.text_FechaFacturaCliente.setText(fecha)
            self.text_NumFacturaCliente.setText(num_factura)
        else:
            
            tam_datos = empresa.tamano_datos_cliente()
            j=0
            lista_nueva_fechas = empresa.recuperar_lista_datos_cliente()
            while j < tam_datos :
                lista_indi_datos = str(lista_nueva_fechas[j]).split("$")
                nombre = lista_indi_datos[0]
                fecha = lista_indi_datos[1]
                direccion = lista_indi_datos[2]
                cedula = lista_indi_datos[3]
                telefono = lista_indi_datos[4]
                num_factura = lista_indi_datos[5]
                j = j+1

            self.text_FechaFacturaCliente.setText(fecha)
            self.text_NumFacturaCliente.setText(num_factura)
            self.text_telefonoCliente.setText(telefono)
            self.text_CedulaCliente.setText(cedula)
            self.text_direccionCliente.setText(direccion)
            self.text_nombreCliente.setText(nombre)
            
        
        tam = empresa.tamano_pedidos_consumidor_final()
        i=0
        j=0
        total = 0.0
        iva = 0.0
        total_iva = 0.0
        lista_nueva = empresa.recuperar_lista_pedidos_consumidor_final()
        while i < tam :
            subtotal = 0.0
            lista_indi = str(lista_nueva[i]).split("$")
            if(num_factura == lista_indi[5]):
                subtotal = float(lista_indi[3])*float(lista_indi[4])
                self.tabla_productos.setItem(j, 0, QTableWidgetItem(str(lista_indi[1])))
                self.tabla_productos.setItem(j, 1, QTableWidgetItem(str(lista_indi[2])))
                self.tabla_productos.setItem(j, 2, QTableWidgetItem(str(lista_indi[3])))
                self.tabla_productos.setItem(j, 3, QTableWidgetItem(str(lista_indi[4])))
                self.tabla_productos.setItem(j, 4, QTableWidgetItem(str(round(subtotal,3))))
                total = total + subtotal
                j = j + 1
            i = i+1
        
        iva = total * 0.12    
        total_iva = total + iva
    
        self.text_SubtotalFacturaCliente.setText(str(round(total,3)))
        self.text_IVAFacturaCliente.setText(str(round(iva,3)))
        self.text_TotalFacturaCliente.setText(str(round(total_iva,3)))
        
        total = 0.0
        iva = 0.0
        total_iva = 0.0
        
        fecha = ""
        num_factura = ""
        nombre = ""
        direccion = ""
        telefono = ""
        cedula = ""
    
    def salir(self):
        self.close()

class Borrarcategoria(QtWidgets.QWidget,Ui_BorrarCategoria):
    def __init__(self,parent=None):
        super(Borrarcategoria,self).__init__(parent)
        self.setupUi(self)
        self.mostrar_categorias()
        self.botonSeleccionar.clicked.connect(self.seleccionar_categoria)
        self.boton_eliminar_categoria.setEnabled(False)
        self.boton_eliminar_categoria.clicked.connect(self.eliminar_categoria)
        self.boton_cancelar_categoria.clicked.connect(self.salir)
     
    def mostrar_categorias(self):
        tam = empresa.tamano_categorias()
        i=0
        lista_nueva = empresa.recuperar_lista_categorias()
        while i < tam :
            lista_indi = str(lista_nueva[i]).split("$")
            self.tabla_categorias.setItem(i, 0, QTableWidgetItem(str(lista_indi[0])))
            self.tabla_categorias.setItem(i, 1, QTableWidgetItem(str(lista_indi[1])))
            i = i+1
    
    def seleccionar_categoria(self):
        
        codigo_seleccionada = ""
        nombre_seleccionada = ""
        
        fila =  self.tabla_categorias.currentRow()
        lista_nueva = empresa.recuperar_lista_categorias()
        tam = empresa.tamano_categorias()
        i=0
        while i < tam:
            lista_indi = str(lista_nueva[i]).split("$")
            if(i == fila):
                nombre_seleccionada = lista_indi[0]
                codigo_seleccionada = lista_indi[1]
                
            i = i+1
        
        self.text_nombre_categoria.setText(nombre_seleccionada)
        self.text_codigo_eliminar.setText(codigo_seleccionada)
        
        lista_verificar = empresa.recuperar_productos_categoria(nombre_seleccionada)
        
        if(len(lista_verificar) == 0):
            self.boton_eliminar_categoria.setEnabled(True)
        else:
            QMessageBox.information(self, "Eliminar Categoria", "No se puede eliminar esta categoria aun quedan productos en esta", QMessageBox.Ok, QMessageBox.Ok)
            
    def eliminar_categoria(self):
        
        codigo_seleccionada = ""
        nombre_seleccionada = ""
        
        fila =  self.tabla_categorias.currentRow()
        lista_nueva = empresa.recuperar_lista_categorias()
        tam = empresa.tamano_categorias()
        i=0
        while i < tam:
            lista_indi = str(lista_nueva[i]).split("$")
            if(i == fila):
                codigo_seleccionada = lista_indi[1]
                nombre_seleccionada = lista_indi[0]
            i = i+1
        
        empresa.eliminar_categoria(codigo_seleccionada)
        QMessageBox.information(self, "Eliminar Categoria", "Se ha eliminado la categoria: "+nombre_seleccionada, QMessageBox.Ok, QMessageBox.Ok)
        self.close()
    
    def salir(self):
        self.close()
        
class Modificarcategoria(QtWidgets.QWidget,Ui_ModificarCategoria):
    def __init__(self,parent=None):
        super(Modificarcategoria,self).__init__(parent)
        self.setupUi(self)
        self.mostrar_categorias()
        self.botonSeleccionar.clicked.connect(self.seleccionar_categoria)
        self.botonModificarCategoria.setEnabled(False)
        self.botonModificarCategoria.clicked.connect(self.modificar_categoria)
        self.botonCancelarcategoria.clicked.connect(self.salir)
        
    def mostrar_categorias(self):
        tam = empresa.tamano_categorias()
        i=0
        lista_nueva = empresa.recuperar_lista_categorias()
        while i < tam :
            lista_indi = str(lista_nueva[i]).split("$")
            self.tabla_categorias.setItem(i, 0, QTableWidgetItem(str(lista_indi[0])))
            self.tabla_categorias.setItem(i, 1, QTableWidgetItem(str(lista_indi[1])))
            i = i+1
    
    def seleccionar_categoria(self):
        
        codigo_seleccionada = ""
        nombre_seleccionada = ""
        descripcion_seleccionada = ""
        
        fila =  self.tabla_categorias.currentRow()
        lista_nueva = empresa.recuperar_lista_categorias()
        tam = empresa.tamano_categorias()
        i=0
        while i < tam:
            lista_indi = str(lista_nueva[i]).split("$")
            if(i == fila):
                nombre_seleccionada = lista_indi[0]
                codigo_seleccionada = lista_indi[1]
                descricpcion_seleccionada = lista_indi[2]
            i = i+1
        
        self.text_categoriaseleccionada.setText(nombre_seleccionada)
        self.text_codigocategoriaseleccionada.setText(codigo_seleccionada)
        self.edit_nombreCategoria.setText(nombre_seleccionada)
        self.edit_descripcionCategoria.setText(descricpcion_seleccionada)
        self.botonModificarCategoria.setEnabled(True)
            
    def modificar_categoria(self):
        
        codigo_seleccionada = ""
        nombre_seleccionada = ""
        
        fila =  self.tabla_categorias.currentRow()
        lista_nueva = empresa.recuperar_lista_categorias()
        tam = empresa.tamano_categorias()
        i=0
        while i < tam:
            lista_indi = str(lista_nueva[i]).split("$")
            if(i == fila):
                codigo_seleccionada = lista_indi[1]
                nombre_seleccionada = lista_indi[0]
            i = i+1
        
        nuevo_nombre_categoria = self.edit_nombreCategoria.text()
        nueva_descricion_categoria = self.edit_descripcionCategoria.text()
        
        empresa.modificar_categoria(nombre_seleccionada,nuevo_nombre_categoria,codigo_seleccionada,nueva_descricion_categoria)
        QMessageBox.information(self, "Modificar Categoria", "Se ha modificado la categoria: "+nombre_seleccionada, QMessageBox.Ok, QMessageBox.Ok)
        self.close()
    
    def salir(self):
        self.close()

class Agregarcategoria(QtWidgets.QWidget,Ui_RegistroCategoria):
    def __init__(self,parent=None):
        super(Agregarcategoria,self).__init__(parent)
        self.setupUi(self)
        self.boton_Siguiente_Datos.clicked.connect(self.guardar_categoria)
        self.boton_Cancelar_Datos.clicked.connect(self.salir)
    
    def guardar_categoria(self):
        nombre = self.edit_nombreCategoria.text()
        codigo = self.edit_codigoCategoria.text()
        descripcion = self.edit_descripcionCategoria.text()
        empresa.agregar_categoria(nombre, codigo, descripcion)
        self.edit_nombreCategoria.clear()
        self.edit_codigoCategoria.clear()
        self.edit_descripcionCategoria.clear()
        empresa.mostrar_categorias()
        QMessageBox.information(self, "Agregar Categoria", "Se ha agregado la categoria: "+nombre, QMessageBox.Ok, QMessageBox.Ok)
        self.close()
    
    def salir(self):
        self.close()

class Borrarproducto(QtWidgets.QWidget,Ui_BorrarProducto):
    def __init__(self,parent=None):
        super(Borrarproducto,self).__init__(parent)
        self.setupUi(self)
        self.mostrar_productos()
        self.comboBox.addItems(empresa.nombres_Categorias())
        self.comboBox.currentTextChanged.connect(self.cambiar_categoria)
        self.botonSeleccionar.clicked.connect(self.seleccionar_producto)
        self.boton_cancelar_producto.clicked.connect(self.salir)
        self.boton_eliminar_producto.setEnabled(False)
        self.boton_eliminar_producto.clicked.connect(self.eliminar_producto)
        
    def cambiar_categoria(self):
        categoria = self.comboBox.currentText()
        if(categoria == "Todas"):
            self.tabla_productos.clearContents()
            self.mostrar_productos()
        else:
            self.tabla_productos.clearContents()
            tam = empresa.tamano_productos()
            i=0
            j=0
            lista_nueva = empresa.recuperar_lista_productos()
            while i < tam :
                lista_indi = str(lista_nueva[i]).split("$")
                if(categoria == lista_indi[0]):
                    self.tabla_productos.setItem(j, 0, QTableWidgetItem(str(lista_indi[1])))
                    self.tabla_productos.setItem(j, 1, QTableWidgetItem(str(lista_indi[2])))
                    self.tabla_productos.setItem(j, 2, QTableWidgetItem(str(lista_indi[3])))
                    self.tabla_productos.setItem(j, 3, QTableWidgetItem(str(lista_indi[4])))
                    j = j+1
                i = i+1
                
    def mostrar_productos(self):
        tam = empresa.tamano_productos()
        i=0
        lista_nueva = empresa.recuperar_lista_productos()
        while i < tam :
            lista_indi = str(lista_nueva[i]).split("$")
            self.tabla_productos.setItem(i, 0, QTableWidgetItem(str(lista_indi[1])))
            self.tabla_productos.setItem(i, 1, QTableWidgetItem(str(lista_indi[2])))
            self.tabla_productos.setItem(i, 2, QTableWidgetItem(str(lista_indi[3])))
            self.tabla_productos.setItem(i, 3, QTableWidgetItem(str(lista_indi[4])))
            i = i+1
        
    def seleccionar_producto(self):
        
        codigo_seleccionado = ""
        producto_seleccionado = ""
        
        categoria = self.comboBox.currentText()
        fila =  self.tabla_productos.currentRow()
        
        if(categoria == "Todas"):
            lista_nueva = empresa.recuperar_lista_productos()
            tam = empresa.tamano_productos()
            i=0
            while i < tam:
                lista_indi = str(lista_nueva[i]).split("$")
                if(i == fila):
                    codigo_seleccionado = lista_indi[2]
                    producto_seleccionado = lista_indi[3]
                i = i+1
            
            self.text_nombre_producto.setText(producto_seleccionado)
            self.text_codigo_eliminar_producto.setText(codigo_seleccionado)
            self.boton_eliminar_producto.setEnabled(True)
            
        else:
            lista_nueva_2 = empresa.recuperar_productos_categoria(categoria)
            tam = empresa.tamano_productos_por_categoria()
            i=0
            while i < tam:
                lista_indi_2 = str(lista_nueva_2[i]).split("$")
                if(i == fila):
                    codigo_seleccionado = lista_indi_2[2]
                    producto_seleccionado = lista_indi_2[3]
                i = i+1
            
            self.text_nombre_producto.setText(producto_seleccionado)
            self.text_codigo_eliminar_producto.setText(codigo_seleccionado)
            self.boton_eliminar_producto.setEnabled(True)
        
    def eliminar_producto(self):
        
        codigo_seleccionado = ""
        producto_seleccionado = ""
        
        categoria = self.comboBox.currentText()
        fila =  self.tabla_productos.currentRow()
        
        if(categoria == "Todas"):
            lista_nueva = empresa.recuperar_lista_productos()
            tam = empresa.tamano_productos()
            i=0
            while i < tam:
                lista_indi = str(lista_nueva[i]).split("$")
                if(i == fila):
                    codigo_seleccionado = lista_indi[2]
                    producto_seleccionado = lista_indi[3]
                i = i+1

            empresa.eliminar_producto(codigo_seleccionado)
            QMessageBox.information(self, "Eliminar Producto", "Se ha eliminado el producto : "+producto_seleccionado, QMessageBox.Ok, QMessageBox.Ok)
            self.close()
        else:
            lista_nueva_2 = empresa.recuperar_productos_categoria(categoria)
            tam = empresa.tamano_productos_por_categoria()
            i=0
            while i < tam:
                lista_indi_2 = str(lista_nueva_2[i]).split("$")
                if(i == fila):
                    codigo_seleccionado = lista_indi_2[2]
                    producto_seleccionado = lista_indi_2[3]
                i = i+1
            
            empresa.eliminar_producto(codigo_seleccionado)
            QMessageBox.information(self, "Eliminar Producto", "Se ha eliminado el producto : "+producto_seleccionado, QMessageBox.Ok, QMessageBox.Ok)
            self.close()
    
    def salir(self):
        self.close()
        
class Modificarproducto(QtWidgets.QWidget,Ui_ModificarProducto):
    def __init__(self,parent=None):
        super(Modificarproducto,self).__init__(parent)
        self.setupUi(self)
        self.mostrar_productos()
        self.comboBox.addItems(empresa.nombres_Categorias())
        self.comboBox.currentTextChanged.connect(self.cambiar_categoria)
        self.botonSeleccionarProducto.clicked.connect(self.seleccionar_producto)
        self.botonCancelarProducto.clicked.connect(self.salir)
        self.botonModificarProducto.setEnabled(False)
        self.botonModificarProducto.clicked.connect(self.modificar_producto)
        
    def cambiar_categoria(self):
        categoria = self.comboBox.currentText()
        if(categoria == "Todas"):
            self.tabla_productos_modificacion.clearContents()
            self.mostrar_productos()
        else:
            self.tabla_productos_modificacion.clearContents()
            tam = empresa.tamano_productos()
            i=0
            j=0
            lista_nueva = empresa.recuperar_lista_productos()
            while i < tam :
                lista_indi = str(lista_nueva[i]).split("$")
                if(categoria == lista_indi[0]):
                    self.tabla_productos_modificacion.setItem(j, 0, QTableWidgetItem(str(lista_indi[1])))
                    self.tabla_productos_modificacion.setItem(j, 1, QTableWidgetItem(str(lista_indi[2])))
                    self.tabla_productos_modificacion.setItem(j, 2, QTableWidgetItem(str(lista_indi[3])))
                    self.tabla_productos_modificacion.setItem(j, 3, QTableWidgetItem(str(lista_indi[4])))
                    j = j+1
                i = i+1
                
    def mostrar_productos(self):
        tam = empresa.tamano_productos()
        i=0
        lista_nueva = empresa.recuperar_lista_productos()
        while i < tam :
            lista_indi = str(lista_nueva[i]).split("$")
            self.tabla_productos_modificacion.setItem(i, 0, QTableWidgetItem(str(lista_indi[1])))
            self.tabla_productos_modificacion.setItem(i, 1, QTableWidgetItem(str(lista_indi[2])))
            self.tabla_productos_modificacion.setItem(i, 2, QTableWidgetItem(str(lista_indi[3])))
            self.tabla_productos_modificacion.setItem(i, 3, QTableWidgetItem(str(lista_indi[4])))
            i = i+1
        
    def seleccionar_producto(self):
        
        producto_seleccionado = ""
        descripcion_seleccionado = ""
        valor_seleccionado = ""
        
        categoria = self.comboBox.currentText()
        fila =  self.tabla_productos_modificacion.currentRow()
        
        if(categoria == "Todas"):
            lista_nueva = empresa.recuperar_lista_productos()
            tam = empresa.tamano_productos()
            i=0
            while i < tam:
                lista_indi = str(lista_nueva[i]).split("$")
                if(i == fila):
                    valor_seleccionado = lista_indi[1]
                    producto_seleccionado = lista_indi[3]
                    descripcion_seleccionado = lista_indi[4]
                i = i+1
            
            self.text_producto_seleccionado.setText(producto_seleccionado)
            self.edit_nombre_producto_modificar.setText(producto_seleccionado)
            self.edit_descripcion_producto_modificar.setText(descripcion_seleccionado)
            self.edit_precio_producto_modificar.setText(valor_seleccionado)
            self.botonModificarProducto.setEnabled(True)
            
        else:
            lista_nueva_2 = empresa.recuperar_productos_categoria(categoria)
            tam = empresa.tamano_productos_por_categoria()
            i=0
            while i < tam:
                lista_indi_2 = str(lista_nueva_2[i]).split("$")
                if(i == fila):
                    valor_seleccionado = lista_indi_2[1]
                    producto_seleccionado = lista_indi_2[3]
                    descripcion_seleccionado = lista_indi_2[4]
                i = i+1
            
            self.text_producto_seleccionado.setText(producto_seleccionado)
            self.edit_nombre_producto_modificar.setText(producto_seleccionado)
            self.edit_descripcion_producto_modificar.setText(descripcion_seleccionado)
            self.edit_precio_producto_modificar.setText(valor_seleccionado)
            self.botonModificarProducto.setEnabled(True)
        
        producto_seleccionado = ""
        descripcion_seleccionado = ""
        valor_seleccionado = ""
        
    def modificar_producto(self):
        
        codigo_seleccionado = ""
        producto_seleccionado = ""
        
        categoria = self.comboBox.currentText()
        fila =  self.tabla_productos_modificacion.currentRow()
        
        if(categoria == "Todas"):
            lista_nueva = empresa.recuperar_lista_productos()
            tam = empresa.tamano_productos()
            i=0
            while i < tam:
                lista_indi = str(lista_nueva[i]).split("$")
                if(i == fila):
                    codigo_seleccionado = lista_indi[2]
                    producto_seleccionado = lista_indi[3]
                i = i+1

            nuevo_nombre_producto = self.edit_nombre_producto_modificar.text()
            nueva_descricion_producto = self.edit_descripcion_producto_modificar.text()
            nuevo_precio_producto = self.edit_precio_producto_modificar.text()

            empresa.modificar_producto(nuevo_nombre_producto,codigo_seleccionado,nueva_descricion_producto,nuevo_precio_producto)
            QMessageBox.information(self, "Modificar Producto", "Se ha modificado el producto : "+producto_seleccionado, QMessageBox.Ok, QMessageBox.Ok)
            self.close()
        else:
            lista_nueva_2 = empresa.recuperar_productos_categoria(categoria)
            tam = empresa.tamano_productos_por_categoria()
            i=0
            while i < tam:
                lista_indi_2 = str(lista_nueva_2[i]).split("$")
                if(i == fila):
                    codigo_seleccionado = lista_indi_2[2]
                    producto_seleccionado = lista_indi_2[3]
                i = i+1
            
            nuevo_nombre_producto = self.edit_nombre_producto_modificar.text()
            nueva_descricion_producto = self.edit_descripcion_producto_modificar.text()
            nuevo_precio_producto = self.edit_precio_producto_modificar.text()
            
            empresa.modificar_producto(nuevo_nombre_producto,codigo_seleccionado,nueva_descricion_producto,nuevo_precio_producto)
            QMessageBox.information(self, "Modificar Producto", "Se ha modificado el producto : "+producto_seleccionado, QMessageBox.Ok, QMessageBox.Ok)
            self.close()
    
    def salir(self):
        self.close()

class Agregarproducto(QtWidgets.QWidget,Ui_IngresoProducto):
    def __init__(self,parent=None):
        super(Agregarproducto,self).__init__(parent)
        self.setupUi(self)
        self.boton_Siguiente_Datos.clicked.connect(self.guardar_producto)
        self.boton_Cancelar_Datos.clicked.connect(self.salir)
        self.comboBox.addItems(empresa.nombres_Categorias())
    
    def guardar_producto(self):
        nombre = self.edit_telefono_2.text()
        precio = self.edit_telefono_3.text()
        codigo = self.edit_cedula_3.text()
        descripcion = self.edit_cedula_4.text()
        categoria = self.comboBox.currentText()
        empresa.agregar_producto(categoria,precio,codigo,nombre, descripcion)
        self.edit_telefono_2.clear()
        self.edit_telefono_3.clear()
        self.edit_cedula_4.clear()
        self.edit_cedula_3.clear()
        empresa.mostrar_productos()
        QMessageBox.information(self, "Agregar Producto", "Se ha agregado el producto :"+nombre,QMessageBox.Ok, QMessageBox.Ok)
        
    def salir(self):
        self.close()


class InformacionVentas(QtWidgets.QMainWindow,Ui_infoventas):
    def __init__(self, parent=None):
        super(InformacionVentas, self).__init__(parent)
        self.setupUi(self)
        self.botonaceptar.clicked.connect(self.salir)
        self.mostrar_productos_vendidos()
        self.comboBox_categorias.addItems(empresa.nombres_Categorias())
        self.comboBox_categorias.currentTextChanged.connect(self.cambiar_categoria_fecha)
        self.comboBox_fechas.addItems(empresa.fechas_ventas_consumidor_final())
        self.comboBox_fechas.addItems(empresa.fechas_ventas_cliente())
        self.comboBox_fechas.currentTextChanged.connect(self.cambiar_categoria_fecha)
    
    def cambiar_categoria_fecha(self):
        categoria = self.comboBox_categorias.currentText()
        fecha = self.comboBox_fechas.currentText()
        if(categoria == "Todas" and fecha == "Todas"):
            self.tabla_ventas.clearContents()
            self.mostrar_productos_vendidos()
        else:
            self.tabla_ventas.clearContents()
            tam = len(empresa.recuperar_clave_producto(categoria))
            i=0
            j=0
            lista_nueva = empresa.recuperar_clave_producto(categoria)
            while i < tam :
                lista_indi = str(lista_nueva[i]).split("$")
                if((lista_indi[4] == empresa.recuperar_clave_fecha(empresa.recuperar_clave_consumidor_final(fecha))) or (lista_indi[4] == empresa.recuperar_clave_fecha(empresa.recuperar_clave_cliente(fecha)))):
                    self.tabla_ventas.setItem(j, 0, QTableWidgetItem(str(lista_indi[4])))
                    self.tabla_ventas.setItem(j, 1, QTableWidgetItem(str(lista_indi[0])))
                    self.tabla_ventas.setItem(j, 2, QTableWidgetItem(str(lista_indi[1])))
                    self.tabla_ventas.setItem(j, 3, QTableWidgetItem(str(lista_indi[2])))
                    self.tabla_ventas.setItem(j, 4, QTableWidgetItem(str(lista_indi[3])))
                    j=j+1
                i = i+1
    
    def mostrar_productos_vendidos(self):
        tam = empresa.tamano_pedidos_consumidor_final()
        i=0
        lista_nueva = empresa.recuperar_lista_pedidos_consumidor_final()
        while i < tam :
            lista_indi = str(lista_nueva[i]).split("$")
            self.tabla_ventas.setItem(i, 0, QTableWidgetItem(str(lista_indi[5])))
            self.tabla_ventas.setItem(i, 1, QTableWidgetItem(str(lista_indi[2])))
            self.tabla_ventas.setItem(i, 2, QTableWidgetItem(str(lista_indi[1])))
            self.tabla_ventas.setItem(i, 3, QTableWidgetItem(str(lista_indi[3])))
            self.tabla_ventas.setItem(i, 4, QTableWidgetItem(str(lista_indi[4])))
            i = i+1
    
    def salir(self):
        self.close()

class AcercaDe(QtWidgets.QMainWindow,Ui_ventanaAcerca):
    def __init__(self, parent=None):
        super(AcercaDe, self).__init__(parent)
        self.setupUi(self)

class Principal(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(Principal, self).__init__(parent)
        self.setupUi(self)
        self.actionRealizar_un_pedido.triggered.connect(self.hacerpedido)
        self.actionVer_informaci_n_de_productos.triggered.connect(self.verproductos)
        self.actionEliminar.triggered.connect(self.eliminarcategoria)
        self.actionModificar.triggered.connect(self.modificarcategoria)
        self.actionAgregar.triggered.connect(self.agregarcategoria)
        self.actionEliminar_2.triggered.connect(self.eliminarproducto)
        self.actionModificar_2.triggered.connect(self.modificarproducto)
        self.actionAgregar_2.triggered.connect(self.agregarproducto)
        self.actionInformaci_n_de_ventas.triggered.connect(self.infotmacion_ventas)
        self.actionVer_Productos.triggered.connect(self.verproductos)
        self.actionCompra.triggered.connect(self.hacerpedido)
        self.actionInformaci_n_de_ventas_2.triggered.connect(self.infotmacion_ventas)
        self.actionSalir.triggered.connect(self.salir)
        self.actionInformacion.triggered.connect(self.acercade)
        
    def closeEvent(self, event):
        resultado = QMessageBox.question(self, "Finalizar Programa", "¿Esta seguro de salir?", QMessageBox.Yes | QMessageBox.No)
        if resultado ==QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    
    def salir(self):
        sys.exit(0)
    
    def verproductos(self):
        self.ventana_ver_productos = VerProductos()
        self.ventana_ver_productos.show()

    def hacerpedido(self):
        self.ventana_hacer_pedido = HacerPedido()
        self.ventana_hacer_pedido.show()
        
    def eliminarcategoria(self):
        self.ventana_eliminar_categoria = Borrarcategoria()
        self.ventana_eliminar_categoria.show()
    
    def modificarcategoria(self):
        self.ventana_modificar_categoria = Modificarcategoria()
        self.ventana_modificar_categoria.show()
    
    def agregarcategoria(self):
        self.ventana_agregar_categoria = Agregarcategoria()
        self.ventana_agregar_categoria.show()
    
    def eliminarproducto(self):
        self.ventana_eliminar_producto = Borrarproducto()
        self.ventana_eliminar_producto.show()
    
    def modificarproducto(self):
        self.ventana_modificar_producto = Modificarproducto()
        self.ventana_modificar_producto.show()
    
    def agregarproducto(self):
        self.ventana_agregar_producto = Agregarproducto()
        self.ventana_agregar_producto.show()

    def infotmacion_ventas(self):
        self.ventana_info_ventas = InformacionVentas()
        self.ventana_info_ventas.show()
    
    def acercade(self):
        self.ventana_info = AcercaDe()
        self.ventana_info.show()

app = QtWidgets.QApplication(sys.argv)
myApp = Principal()
myApp.show()
app.exec_()