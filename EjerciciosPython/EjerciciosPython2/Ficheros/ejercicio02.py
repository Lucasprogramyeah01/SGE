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

cotizacionCSV = open("./EjerciciosPython2/Ficheros/cotizacion.csv", "r+")

with open("./EjerciciosPython2/Ficheros/cotizacion.csv", "r+") as cotizacionCSV:
    lectorCSV = csv.DictReader(cotizacionCSV)

    

    data = [column for row in csv_reader]
print(data)

#print(cotizacionCSV.read())









