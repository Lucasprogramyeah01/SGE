import math

# Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos
# en el plano. Calcula y muestra la distancia entre ellos.

x1 = float(input("Introduzca la coordenada x del primer punto: "))
y1 = float(input("Introduzca la coordenada y del segundo punto: "))

x2 = float(input("\nIntroduzca el coordenada x del segundo punto: "))
y2 = float(input("Introduzca el coordenada y del segundo punto: "))

distancia = math.sqrt(((x2-x1)**2)+((y2-y1)**2))

print("\nLa distancia entre los dos puntos es de: %.2f unidades." %(distancia))