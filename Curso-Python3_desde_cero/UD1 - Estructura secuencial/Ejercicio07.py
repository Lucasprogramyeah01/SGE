# Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a
# cuantas horas y minutos corresponde.

min = float(input("Introduzca una cantidad de minutos: "))

horas = min/60
seg = min*60

print("%.2f minutos son %.2f horas o %.2f segundos." %(min, horas, seg))
