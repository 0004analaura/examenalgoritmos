import openpyxl
import os



# ============ Vehiculos ============
#cargamos el documento excel
libro = openpyxl.load_workbook('vehiculos.xlsx')

#abrimos una hoja
hoja = libro['Listado']

 #crear encabezado
hoja['A1'].value ="Id"
hoja['B1'].value ="Codigo"
hoja['C1'].value =  "Marca"
hoja['D1'].value =  "Modelo"
hoja['E1'].value =  "Precio"
hoja['F1'].value =  "Kilometraje"


datos_ejemplo = [

    {
        'Id': 1,
        "Codigo": "001", 
        "Marca": "Toyota",
        "Modelo": "2018",
        "Precio": "20000",
        "Kilometraje": "30000",

    }

]
# no posicionamos en la fila 2 del excel
proxima_fila = hoja.max_row + 1

for venta in datos_ejemplo:
    hoja[f'A{proxima_fila}'].value = venta['Id']
    hoja[f'B{proxima_fila}'].value = venta['Codigo']
    hoja[f'C{proxima_fila}'].value = venta['Marca']
    hoja[f'D{proxima_fila}'].value = venta['Modelo']
    hoja[f'E{proxima_fila}'].value = venta['Precio']
    hoja[f'F{proxima_fila}'].value = venta['Kilometraje']
    proxima_fila +=1



    

#guardar el archivo
libro.save("vehiculos.xlsx")