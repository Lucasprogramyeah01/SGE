# Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de
# números a introducir). El programa debe informar de cuantos números introducidos
# son mayores que 0, menores que 0 e iguales a 0.

cantNumMayor0 = 0
cantNumIgual0 = 0
cantNumMenor0 = 0

cantidadNum = int(input("Introduzca la cantidad de números a meter: "))

i=0
for let in range(i, cantidadNum):
    num = float(input("Introduzca un número: "))

    if num > 0:
        cantNumMayor0 += 1
    elif num < 0:
        cantNumMenor0 += 1
    else:
        cantNumIgual0 += 1

    i += 1

print("\nResultado:\n"
      "Números mayores que 0:",cantNumMayor0,"\n"
      "Números iguales a 0:",cantNumIgual0,"\n"
      "Números menores que 0:",cantNumMenor0)