# Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.

num = float(input("Introduzca un valor en grados Fahrenheit: "))

conversion = (num-32)/1.8

print("%.2f ºF serían %.2f ºC." %(num, conversion))
