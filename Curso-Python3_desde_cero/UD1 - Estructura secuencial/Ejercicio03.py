import math

# Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

cateto1 = float(input("Introduzca la medida del primer cateto: "))
cateto2 = float(input("Introduzca la medida del segundo cateto: "))

hipotenusa = math.sqrt((cateto1**2)+(cateto2**2))

print("La hipotenusa del triángulo es de: %.2f m" %(hipotenusa))