# Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma
# y la media de todos los números introducidos.

num = 1
cuentaNum=0
suma = 0

while num!=0:
    num = float(input("Introduzca un número (0 para salir): "))

    if num!=0:
        cuentaNum += 1

        suma += num
        media = suma/cuentaNum

        print("\nLa suma de los números introducidos es: %.2f." %suma)
        print("La media de los números introducidos es: %.2f.\n" % media)
