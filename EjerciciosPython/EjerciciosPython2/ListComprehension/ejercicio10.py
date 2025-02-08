"""
EJERCICIO 10
---------------------------------------------------------------------------------------------------------
Encuentra todas las palabras en una cadena que tengan menos de 4 letras.
"""

cadena = input("Intoduzca el mensaje que desee:\n")

listaPalabrasEncontradas = list(p for p in cadena.split(" ") if len(p) < 4)

print(listaPalabrasEncontradas)
