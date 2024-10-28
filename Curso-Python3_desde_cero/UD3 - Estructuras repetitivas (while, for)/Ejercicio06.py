# Escribir un programa que imprima todos los números pares entre dos números que
# se le pidan al usuario.

listaNum = []

num1 = int(input("Introduzca el primer número: "))
num2 = int(input("Introduzca el segundo número: "))

numBucle = num1

for let in range(num1, num2):
    numBucle += 1

    if numBucle%2 == 0 and numBucle!=num2:
        listaNum.append(numBucle)

print("\nLos números pares entre",num1,"y",num2,"son:",listaNum)