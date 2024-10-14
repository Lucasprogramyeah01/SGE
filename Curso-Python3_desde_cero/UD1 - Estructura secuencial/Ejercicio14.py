# Dado un número de dos cifras, diseñe un algoritmo que permita obtener el
# número invertido.

num = input("Introduzca un número entero de dos cifras: ")

numeroInverso = int(num[1] + num[0])

print("El número invertido de",num,"es:",numeroInverso,".")