# Escribe un programa que lea un número e indique si es par o impar.

num = int(input("Introduzca un número: "))

if num%2 == 0:
    print(num,"es un número PAR.")
else:
    print(num, "es un número IMPAR.")