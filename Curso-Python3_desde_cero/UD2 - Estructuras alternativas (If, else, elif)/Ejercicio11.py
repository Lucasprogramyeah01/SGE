# Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las
# dimensiones de los lados de un triángulo.
# El programa debe determinar que tipo de triángulo es, teniendo en cuenta:
# Si se cumple Pitágoras entonces es triángulo rectángulo
# Si sólo dos lados del triángulo son iguales entonces es isósceles.
# Si los 3 lados son iguales entonces es equilátero.
# Si no se cumple ninguna de las condiciones anteriores, es escaleno.

ladoA = float(input("Introduzca la longitud del primer lado del triángulo: "))
ladoB = float(input("Introduzca la longitud del segundo lado del triángulo: "))
ladoC = float(input("Introduzca la longitud del tercer lado del triángulo: "))

if (ladoA**2)+(ladoB**2)==(ladoC**2) or (ladoA**2)+(ladoC**2)==(ladoB**2) or (ladoC**2)+(ladoB**2)==(ladoA**2):
    print("\nEl triángulo es RECTÁNGULO.")
elif (ladoA == ladoB and ladoB == ladoC):
    print("\nEl triángulo es EQUILÁTERO.")
elif (ladoA == ladoB and ladoC != ladoA) or (ladoA == ladoC and ladoB != ladoA) or (ladoB == ladoC and ladoA != ladoB):
    print("\nEl triángulo es ISÓSCELES.")
else:
    print("\nEl triángulo es ESCALENO.")