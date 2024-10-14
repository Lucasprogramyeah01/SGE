# Algoritmo que pida un número y diga si es positivo, negativo o 0.

num = int(input("Introduzca un número: "))

if num>0:
    print(num,"es un número positivo.")
elif num<0:
    print(num, "es un número negativo.")
else:
    print(num, "es igual a 0.")