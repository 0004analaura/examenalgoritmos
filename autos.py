import os
import openpyxl
import sys


# ============ Vehiculos ============

def crearVehiculos(codigo, marca, modelo,  precio, kilometraje):
    def comprobarProducto(codigo):
        if os.path.exists("vehiculos.txt"):
            with open("vehiculos.txt", "r") as productos:
                for vehiculo in vehiculo:
                    if vehiculo.split("|")[0] == codigo:
                        return True
        return False
    if comprobarProducto(codigo):
        print("El producto ", codigo, " ya existe")
    else:
        with open("vehiculos.txt", "a") as productos:
            productos.write(codigo + "|" + marca + "|" +
                            modelo + "|" + precio + "|" + kilometraje + "\n")
        print("Producto " , codigo, " agregado")     


def listarVehiculos():
    # Leer el archivo productos.txt
    productos = open("vehiculos.txt", "r")
    print("====== Productos ======")
    for producto in productos:
        print(producto)
    print("=======================")
    productos.close()     



def actualizarVehiculo(codigo, marca, modelo,  precio, kilometraje):
    # Actualizar los datos parametrados en un archivo productos.txt
    productos = open("vehiculos.txt", "r")
    productosTemp = open("productosTemp.txt", "w")
    for producto in productos:
        if producto.split("|")[0] == codigo:
            productosTemp.write(codigo + "|" + marca + "|" +
                                modelo + "|" + precio + "|" + kilometraje + "\n")
        else:
            productosTemp.write(producto)
            print("Producto ", codigo, " actualizado exitosamente")
    productos.close()
    productosTemp.close()
    os.remove("vehiculos.txt")
    os.rename("productosTemp.txt", "vehiculos.txt")   


def eliminarVehiculos(codigo):
    # Eliminar los datos parametrados en un archivo productos.txt
    productos = open("vehiculos.txt", "r")
    productosTemp = open("productosTemp.txt", "w")
    for producto in productos:
        if producto.split("|")[0] != codigo:
            productosTemp.write(producto)
            print("Producto ",codigo, " eliminado exitosamente")
    productos.close()
    productosTemp.close()
    os.remove("vehiculos.txt")
    os.rename("productosTemp.txt", "vehiculos.txt")     

def reporteVentasVehiculos(codigo_vehiculo):
   
    workbook = openpyxl.Workbook()
  
    worksheet= workbook.worksheets[0]
   
    worksheet["A1"]="Codigo"
    worksheet["B1"]="Marca"
    worksheet["C1"]="Modelo"
    worksheet["D1"]="Precio"
    worksheet["E1"]="Kilomettaje"



    columnas=("A", "B", "C", "D", "E", "F")
    row = 2
    with open("vehiculos.txt", "r") as archivoVehiculos:
        ventas = archivoVehiculos.readlines()
    for vehiculos in vehiculos:

        datos=vehiculos.split("|")
        if(datos[2]!=codigo_vehiculo):
            continue
        worksheet.insert_rows(row)
        for i  in range (len(datos)):

            col=columnas[i] +str(row)
            print(col + str(row))
            worksheet[col]=datos[i]


        row += 1

    workbook.save("vehiculos.xlsx")
    workbook.close()

# ==================== Menu ====================
# Crear un menu con todas las funciones y un submenu con las funciones de cada seccion
def menu():
    print("""

==================== Menu ====================""")
    print("1. Clientes")
    print("2. Productos")
    print("3. Ventas")
    print("4. Reportes")
    print("5. Salir")
    print("""
=============================================""")
    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        menuVentas()
  
        print("""

Gracias por usar el sistema

""")
        exit()
    else:
        print("""

Opcion no valida

""")
        menu()

# ==================== Menu Clientes ====================
# Crear un submenu con las funciones de clientes
def menuVentas():

    print("""

==================== Clientes ====================""")
    print("1. Agregar Vehiculo")
    print("2. Editar Vehiculo")
    print("3. Eliminar Vehiculo")
    print("4. Listar Vehiculo")
    print("""

=============================================""")
    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        # codigo, marca, modelo, precio, kilometraje
        codigo = input("Ingrese el codigo del codigo: ")
        marca = input("Ingrese la marca del vehiculo: ")
        modelo = input("Ingrese el modelo del vehiculo: ")
        precio = input("Ingrese el precio del vehiculo: ")
        kilometraje = input("Ingrese el kilometraje del vehiculo: ")
        crearVehiculos(codigo, marca, modelo, precio, kilometraje)
        menuVentas()
    elif opcion == "3":
        codigo = input("Ingrese el codigo del cliente a eliminar: ")
        eliminarVehiculos(codigo)
        menuVentas()
    elif opcion == "4":
        listarVehiculos()
        menuVentas()
    elif opcion == "5":
        menu()
    else:
        print("""

Opcion no valida

""")
        menu()

def principal():
    if not len(sys.argv) >= 2:
        menu()
    else:
        menu()



