# Calcular el perímetro y área de un rectángulo dada su base y su altura.

base = float(input("Introduzca la base del rectángulo: "))
altura = float(input("Introduzca la altura del rectángulo: "))

perimetro = (2*base)+(2*altura)
area = (base*altura)

print("El perímetro del rectángulo es de %.2f m y el área es de %.2f m^2." %(perimetro, area))

