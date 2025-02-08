"""
EJERCICIO 7
---------------------------------------------------------------------------------------------------------
Obtén solamente los números en una oración como "En 1984 hubo 13 casos de protesta con más de 
1000 asistentes".
"""

oracion = "En 1984 hubo 13 casos de protesta con más de 1000 asistentes"

listaOracionDividida = oracion.split(" ")

listaNumeros = list(e for e in listaOracionDividida if e.isnumeric())

print(listaNumeros)
