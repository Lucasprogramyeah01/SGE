"""
EJERCICIO 6
---------------------------------------------------------------------------------------------------------
Crea una función que reciba dos array, un booleano y retorne un array.
    - Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.
    - Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.
    - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
"""

def obtenerBoleano(eleccion):
    resultado = True
    
    if(eleccion.upper() == "V"):
        return resultado
    else: 
        resultado = False
        return resultado

def recogerElementosDeArray(booleano, array1, array2):

    arrayResultante = list()

    if(booleano is True):
        for elemento1 in array1:
            for elemento2 in array2:
                if(elemento1 == elemento2):
                    if(elemento1 not in arrayResultante):    
                        arrayResultante.append(elemento1)
    else:
        for elemento1 in array1:
            if elemento1 not in array2:
                arrayResultante.append(elemento1)
        for elemento2 in array2:
            if elemento2 not in array1:
                arrayResultante.append(elemento2)

    return arrayResultante

#---------------------------------------------------------------------------------------------------------------------

elementos1 = input("Introduzca los elementos del primer array:\n")
elementos2 = input("\nIntroduzca los elementos del segundo array:\n")

array1 = elementos1.split(" ")
array2 = elementos2.split(" ")

while True:
    
    eleccion = input("""
-----------------------------------------------
ESCOJA UNA OPCIÓN: 
-----------------------------------------------
V - Ver elementos en común de los array.
F - Ver elementos desiguales de los array.
-----------------------------------------------
""")
    
    if(eleccion.upper() == "V" or eleccion.upper() == "F"):
        break
    else:
        print("\nPor favor, eescoja una de las opciones disponibles.")

print(recogerElementosDeArray(obtenerBoleano(eleccion), array1, array2))
