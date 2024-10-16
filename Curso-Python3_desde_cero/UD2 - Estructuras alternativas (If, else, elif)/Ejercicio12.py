# Escribir un programa que lea un año indicar si es bisiesto.
# Nota: un año es bisiesto si es un número divisible por 4, pero no si es
# divisible por 100, excepto que también sea divisible por 400.

anho = int(input("Introduzca un año: "))

if (anho%4 == 0 and anho%100 != 0) or anho%400 == 0:
    print("El",anho,"es un año bisiesto.")
else:
    print("El",anho,"NO es un año bisiesto.")