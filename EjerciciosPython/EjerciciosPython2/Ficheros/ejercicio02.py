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
en formato csv con el mínimo, el máximo y la media de cada columna.
"""

# ACLARACIÓN: ESTÁ T0DO LLENO DE APUNTES QUE HE IDO HACIENDO A MEDIDA QUE REALIZABA EL EJERCICIO, 
# HAN SIDO VITALES PARA ENTENDER QUÉ ESTABA HACIENDO.

import csv

def leerFichero():
    listaCotizaciones = list()
    with open("./EjerciciosPython2/Ficheros/cotizacion.csv", newline="", encoding="utf-8") as cotizacionCSV:
        reader = csv.DictReader(cotizacionCSV, delimiter=';')
        for row in reader:
            cotizacion = {

                # UNA "row" SE VE ASÍ: {'Nombre': 'ACCIONA', 'Final': '95,95', 'Máximo': '96,75', 'Mínimo': '94,4', 'Volumen': '84.962', 'Efectivo': '8166,11'}

                "nombre": row["Nombre"],

                # ACLARACIÓN: Todos los datos del fichero.csv vienen convertidos en Strings, por lo que necesitamos parsear a float 
                # aquellos que sean datos numéricos.

                    # Para ello, cogemos el valor de cada columna de cada fila y reemplazamos los puntos (que en el fichero
                    # se utilizan para separar los bloques de 3 cifras de un número) por un "sin espacio" para convertir
                    # dicho número en uno entero, y luego reemplazamos las comas por puntos, ya que en Python los números
                    # decimales seperan su parte entera de la decimal con un punto, no con una coma.
           
                    # EJEMPLO: 3.345.234,56 -> 3345234,56 -> 3345234.56

                "final": float(row["Final"].replace('.', '').replace(',', '.')),
                "maximo": float(row["Máximo"].replace('.', '').replace(',', '.')),
                "minimo": float(row["Mínimo"].replace('.', '').replace(',', '.')),
                "volumen": float(row["Volumen"].replace('.', '').replace(',', '.')),
                "efectivo": float(row["Efectivo"].replace('.', '').replace(',', '.'))
            }
            listaCotizaciones.append(cotizacion)

    return listaCotizaciones

def mostrarCotizacionesPorColumnas(listaCotizaciones):
    columnas = {"nombre": [], "final": [], "maximo": [], "minimo": [], "volumen": [], "efectivo": []}
    for cotizacion in listaCotizaciones:

        # UNA "cotizacion" SE VE ASÍ: {'nombre': 'ACCIONA', 'final': 95.95, 'maximo': 96.75, 'minimo': 94.4, 'volumen': 84962.0, 'efectivo': 8166.11}

        for key in columnas.keys():
            columnas[key].append(cotizacion[key]) 

        # EN UNA SOLA ITERACIÓN DEL BUCLE "for cotizacion in listaCotizaciones":

            # Entramos en el bulce "for key in columnas.keys()".

            # En la primera iteración de dicho bucle:
                # key = 'nombre'
                # Le añadimos cotizacion[key] (cotizacion['nombre'] = 'ACCIONA') a columnas[key], o sea columnas['nombre'].
                # O sea que ahora: columnas['nombre'] = ['ACCIONA'].
            
            # En la segunda iteración de dicho bucle:
                # key = 'final'
                # Le añadimos cotizacion[final] (cotizacion['final'] = 95.95) a columnas[key], o sea columnas['final'].
                # O sea que ahora: columnas['final'] = [95.95].

            # Y así con todas las key disponibles...
            
        # LA ITERACIÓN ANTERIOR SERÍA LA PRIMERA DEL BUCLE "for cotizacion in listaCotizaciones", 
        # PARA LA SEGUNDA:

            # key = 'nombre'
            # Le añadimos cotizacion['nombre'] = 'ACERINOX' a columnas['nombre'].
            # O sea que ahora: columnas['nombre'] = ['ACCIONA', 'ACENIROX'].

            # Y así con todas las key disponibles...

            # EL RESULTADO SERÍA: {'nombre': ['ACCIONA', 'ACERINOX'], 'final': [95.95, 8668.0], ... }

    return columnas

def crearFicheroCotizacionesPorColumnas(columnas):
    with open("./EjerciciosPython2/Ficheros/cotizacionesPorColumnas.csv", "w", newline="", encoding="utf-8") as cotPorColCSV:
        writer = csv.writer(cotPorColCSV)
        writer.writerow(["Columna", "Mínimo", "Máximo", "Media"])

        #Con el método writerow() escribimos las columnas que queremos en la primera fila del nuevo fichero.

        for key in columnas.keys():
            if key != 'nombre':
                writer.writerow([key, min(columnas[key]), max(columnas[key]), sum(columnas[key]) / len(columnas[key])])
        
        # EN UNA SOLA ITERACIÓN DEL BUCLE "for key in columnas.keys():

            # Comprobar si la key de la iteración es distinta de 'nombre', ya que es la única key que no contiene
            # una lista de datos númericos. 'nombre' contiene como valor una lista de Strings.

            # Si key == 'nombre' simplemente no se hace nada.
            # Y si key != 'nombre:

            # Introducimos en una fila el nombre, el mínimo, el máximo, y la media de la key correspondiente.

            # Y así con todas las key disponibles...

#---------------------------------------------------------------------------------------------------------------------

cotizaciones = leerFichero()
print(cotizaciones)

columnas = mostrarCotizacionesPorColumnas(cotizaciones)
print(f"\n{columnas}")

crearFicheroCotizacionesPorColumnas(columnas)
