"""
EJERCICIO 3
---------------------------------------------------------------------------------------------------------
Contar el número de espacios en una cadena.
"""

cadena = input("Intoduzca el mensaje que desee:\n")

listaEspacios = list(c for c in list(cadena) if c == " ")

print(f"\nLos espacios en la cadena son: {len(listaEspacios)}.")
