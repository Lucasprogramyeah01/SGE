"""
EJERCICIO 2
---------------------------------------------------------------------------------------------------------
El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 con las siguientes columnas: 
    - Nombre (nombre de la empresa), 
    - Final (precio de la acción al cierre de bolsa), 
    - Máximo (precio máximo de la acción durante la jornada), 
    - Mínimo (precio mínimo de la acción durante la jornada), 
    - Volumen (Volumen al cierre de bolsa), 
    - Efectivo (capitalización al cierre en miles de euros).

Construir una función reciba el fichero de cotizaciones y devuelva un diccionario con los datos del 
fichero por columnas.

Construir una función que reciba el diccionario devuelto por la función anterior y cree un fichero 
en formato csv con el mínimo, el máximo y la media de dada columna.
"""

import csv

"""cotizacionCSV = open("./EjerciciosPython2/Ficheros/cotizacion.csv", "r+")

with open("./EjerciciosPython2/Ficheros/cotizacion.csv", "r+") as cotizacionCSV:
    lectorCSV = csv.DictReader(cotizacionCSV)

    data = [column for row in csv_reader]
print(data)

print(cotizacionCSV.read())"""

import csv

def leerFichero():
    listaCotizaciones = list()
    with open("./EjerciciosPython2/Ficheros/cotizacion.csv", newline="", encoding="utf-8") as cotizacionCSV:
        reader = csv.DictReader(cotizacionCSV, delimiter=';')
        for row in reader:
            cotizacion = {

                # UNA "row" SE VE ASÍ: {'Nombre': 'ACCIONA', 'Final': '95,95', 'Máximo': '96,75', 'Mínimo': '94,4', 'Volumen': '84.962', 'Efectivo': '8166,11'}

                "nombre": row["Nombre"],

                #ACLARACIÓN: Todos los datos del fichero.csv vienen convertidos en Strings, por lo que necesitamos parsear a float aquellos que sean datos numéricos.
                #            Para ello, cogemos 

                "final": float(row["Final"].replace('.', '').replace(',', '.')),
                "maximo": float(row["Máximo"].replace('.', '').replace(',', '.')),
                "minimo": float(row["Mínimo"].replace('.', '').replace(',', '.')),
                "volumen": float(row["Volumen"].replace('.', '').replace(',', '.')),
                "efectivo": float(row["Efectivo"].replace('.', '').replace(',', '.'))
            }
            listaCotizaciones.append(cotizacion)
            print(row) 
    return listaCotizaciones

def mostrarCotizacionesPorColumnas(listaCotizaciones):
    columnas = {"nombre": [], "final": [], "maximo": [], "minimo": [], "volumen": [], "efectivo": []}
    for cotizacion in listaCotizaciones:
        for key in columnas.keys():
            columnas[key].append(cotizacion[key]) 
    return columnas

def crear_fichero_cotizaciones_por_columnas(columnas):
    with open("./EjerciciosPython2/Ficheros/cotizaciones_por_columnas.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Columna", "Mínimo", "Máximo", "Media"])
        for key in columnas.keys():
            if columnas[key]:  
                writer.writerow([key, min(columnas[key]), max(columnas[key]), sum(columnas[key]) / len(columnas[key])])
            else:
                print(f"La columna {key} está vacía y no se puede calcular el mínimo, máximo y media.")

def menu():
    cotizaciones = leerFichero()
    columnas = mostrarCotizacionesPorColumnas(cotizaciones)
    #crear_fichero_cotizaciones_por_columnas(columnas)

menu()







