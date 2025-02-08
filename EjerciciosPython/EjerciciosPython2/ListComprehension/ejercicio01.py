"""
EJERCICIO 1
---------------------------------------------------------------------------------------------------------
Encuentra todos los números del 1 al 1000 que sean divisibles por 7.
"""

listaNumeros = list(range(1, 1001))

listaNumerosDivisibles7 = list(n for n in listaNumeros if n%7 == 0)

print(listaNumerosDivisibles7)
