"""
EJERCICIO 8
---------------------------------------------------------------------------------------------------------
Dado numbers = range(20), se genera una lista que contiene la palabra "par" si un número en los números 
es par, y la palabra "impar" si el número es impar. El resultado se vería así: "impar", "par", "impar".
"""

# ACLARACIÓN: He realizado este ejercicio de dos formas diferentes porque veía ambas muy claras.

numbers = range(20)

# PRIMERA FORMA:
listaParidad = list("par" if n%2 == 0 else "impar" for n in numbers)

# SEGUNDA FORMA:
def comprobarParidad (n):
    if(n%2 == 0):
        return "par"
    else:
        return "impar"

listaParidad2 = list(map(comprobarParidad, numbers))

print(listaParidad)
print(listaParidad2)
