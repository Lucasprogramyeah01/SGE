
import csv
from datetime import datetime
from math import sqrt
from collections import namedtuple

#(AP) - Definimos el objeto, es como un constructor de Java.
Avistamiento = namedtuple('Avistamiento', 'fechahora, ciudad, estado, forma, duracion, comentarios, latitud, longitud')

#(AP) - Definimos una función a la que le pasamos como parámetro la ruta por la que se accede al fichero csv.
def lee_avistamientos(fichero) :

    #(AP) - Queremos que la función nos devuelva una lista de avistamientos, por lo que creamos primero una lista llamada "res".
    res = []

    #(AP) - Abrimos el fichero y le vamos a llamar "f" a partir de ahora. ES BÁSICAMENTE HACER ESTO: f = open(fichero, encoding = 'utf-8');
    #(AP) - El fichero está codificado en utf-8, necesario para leerlo. Además el método open lo pide.
    with open(fichero, encoding = 'utf-8') as f :
        lector = csv.reader(f)      #Esta sentencia crea una lista para cada línea del fichero.
        next(lector)                #Salta la primera línea del fichero.

        #(AP) Vamos cogiendo con un bucle los datos del fichero y los guardamos en variables para conformar un objeto "Avistamiento" al que llamamos "tupla", y este lo metemos en nuestra lista "res" (recoredemos que "res" es una lista de avistamientos).
        #(AP) Nuestro objeto "Avistamiento" necesita todos sus atributos en Strings (tal y como se ve en el constructor) por lo que todos los datos del docuemnto que no sean String los casteamos a String.
        for x in lector :
            fecha_hora = x[0]
            fechahora = datetime.strptime(fecha_hora, '%m/%d/%Y %H:%M')
            ciudad = x[1]
            estado = x[2]
            forma = x[3]
            duracion = int(x[4])
            comentarios = x[5]
            latitud = float(x[6])
            longitud = float(x[7])
            tupla = Avistamiento(fechahora, ciudad, estado, forma, duracion, comentarios, latitud, longitud)
            res.append(tupla)

        return res


#EJERCICIO 2
#En este ejercicio, un registro es un avistamiento.

def duracion_total(registros, estado):

    duracionTotal = 0

    for x in registros:
        if(x.estado == estado):
            duracionTotal += x.duracion

        return duracionTotal

#EJERCICIO 3

def comentario_mas_largo(registros, anyo, palabra):

    """for x in registros:
        if(x.comentario)"""


"""EJERCICIO 4
indexa_formas_por_mes(registros): devuelve un diccionario que indexa las
distintas formas de avistamientos por los nombres de los meses en que se
producen. Por ejemplo, para el mes "Enero" se tendrá un conjunto con todas las
formas distintas observadas en dicho mes."""

def indexa_formas_por_mes(registros):
    diccionario = {}

    for avistamiento in registros:
        # Obtener el nombre del mes
        mes = avistamiento.fechaHora.strftime('%B')

        # Añadir la forma al conjunto correspondiente al mes
        if mes not in diccionario:
            diccionario[mes] = set()

        diccionario[mes].add(avistamiento.forma)

    return diccionario










