"""
EJERCICIO 6
---------------------------------------------------------------------------------------------------------
Encuentra los números comunes en dos listas (sin usar una tupla o conjunto): 
    - lista_a = 1, 2, 3, 4
    - lista_b = 2, 3, 4, 5
"""

lista_a = [1, 2, 3, 4]
lista_b = [2, 3, 4, 5]

listaNumerosComunes = list(n for n in lista_a if n in lista_b)

print(listaNumerosComunes)
