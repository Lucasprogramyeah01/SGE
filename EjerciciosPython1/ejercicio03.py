"""
EJERCICIO 3
---------------------------------------------------------------------------------------------------------
Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima otras dos cadenas como salida (out1, out2).
    - out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
    - out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.
"""

nuevaLista1 = list()
nuevaLista2 = list()

def filtrarCaracteres(str1, str2):

    for caracter in lista1:
        if(caracter in str1 and caracter not in str2):
            if(caracter not in nuevaLista1):
                nuevaLista1.append(caracter)
    
    for caracter in lista2:
        if(caracter in str2 and caracter not in str1):
            if(caracter not in nuevaLista2):
                nuevaLista2.append(caracter)

    return print(f"""
Out1: {delimitador.join(nuevaLista1)} 
Out2: {delimitador.join(nuevaLista2)}
""")

#---------------------------------------------------------------------------------------------------------------------

str1 = input("Introduzca la primera cadena de caracteres:").upper()
str2 = input("\nIntroduzca la segunda cadena de caracteres:").upper()

lista1 = list(str1)
lista2 = list(str2)

delimitador = ""

filtrarCaracteres(str1, str2)
