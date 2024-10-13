# Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.

numero1 = float(input("Introduzca el primer número: "))
numero2 = float(input("Introduzca el segundo número: "))

suma = numero1+numero2
resta = numero1-numero2
producto = numero1*numero2
division = numero1/numero2

print("\nLa suma de los números es: %.2f\n"
      "La resta de los números es: %.2f\n"
      "La multiplicación de los números es: %.2f\n"
      "La división de los números es: %.2f\n"
      %(suma, resta, producto, division))