# Pide al usuario dos números y muestra la "distancia" entre ellos
# (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).

num1 = float(input("Introduzca el primer número: "))
num2 = float(input("Introduzca el segundo número: "))

distancia = abs((num1-num2))

print("La distancia entre los dos números es de: %.2f unidades." %(distancia))