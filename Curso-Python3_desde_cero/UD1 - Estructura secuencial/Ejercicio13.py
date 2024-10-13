import math

# Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica.
# Python3 no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿Cómo se podría calcular?

num = float(input("Introduzca un número: "))

raizCuadrada = math.sqrt(num)
raizCubica = num**(1/3)

print("\nLa raíz cuadrada de %.2f es: %.2f." %(num, raizCuadrada))
print("La raíz cúbica de %.2f es: %.2f." %(num, raizCubica))