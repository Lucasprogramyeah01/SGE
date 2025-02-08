"""
EJERCICIO 2
---------------------------------------------------------------------------------------------------------
Encuentra todos los números del 1 al 1000 que incluyan entre sus cifras al menos un 3.
"""

listaNumeros = list(range(1, 1000))

ListaNumerosEnString = list(map(str, listaNumeros))

listaNumerosFiltrados = list(n for n in ListaNumerosEnString if "3" in n)

print(listaNumerosFiltrados)
