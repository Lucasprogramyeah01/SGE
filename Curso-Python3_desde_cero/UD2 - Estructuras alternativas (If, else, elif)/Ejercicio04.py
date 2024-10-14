# Crea un programa que pida al usuario dos números y muestre su división
# si el segundo es cero, muestre un mensaje de aviso nulo en ese caso.

num1 = float(input("Introduzca el primer número: "))
num2 = float(input("Introduzca el segundo número: "))

if num2 != 0:
    print("\nEl cociente de la división entre %.2f y %.2f es: %.2f." %(num1, num2, num1/num2))
else:
    print("\nEl denominador de la división no puede ser 0 ¡sería una indeterminación!")