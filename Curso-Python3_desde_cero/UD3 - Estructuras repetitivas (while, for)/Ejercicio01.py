# Crea una aplicación que pida un número y calcule su factorial (El factorial de
# un número es el producto de todos los enteros entre 1 y el propio número y se
# representa por el número seguido de un signo de exclamación.
# Por ejemplo 5! = 1x2x3x4x5=120)

num = int(input("Introduzca el número del que desea saber su factorial: "))

numFactorial = 1

i = 0

#El bucle no se realiza para el valor máximo impuesto en el "for".
#En este caso i=0 y num, por ejemplo, igual a 2. Las iteraciones serían i=0 -> i=1, i=1 -> i=2
# Y PARA EN EL VALOR MÁXIMO IMPUESTO.
for let in range (i, num):
    numFactorial = numFactorial*i
    i += 1

print("\nEl factorial de", num, "es", numFactorial,".")