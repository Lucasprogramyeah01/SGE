# Algoritmo que pida tres números y los muestre ordenados (de mayor a menor).

num1 = float(input("Introduzca el primer número: "))
num2 = float(input("Introduzca el segundo número: "))
num3 = float(input("Introduzca el tercer número: "))

numeros = [num1, num2, num3]

numeros.sort(reverse=True)

print("\n",numeros[0],">",numeros[1],">",numeros[2])
