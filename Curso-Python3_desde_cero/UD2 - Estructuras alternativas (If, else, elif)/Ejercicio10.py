import math

# Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos
# circunferencias y las clasifique en uno de estos estados:
# exteriores
# tangentes exteriores
# secantes
# tangentes interiores
# interiores
# concéntricas

x1 = float(input("Introduzca la coordenada x del centro de la primera circunferencia: "))
y1 = float(input("Introduzca la coordenada y del centro de la primera circunferencia: "))
r1 = float(input("Introduzca el radio de la primera circunferencia: "))

x2 = float(input("\nIntroduzca la coordenada x del centro de la segunda circunferencia: "))
y2 = float(input("Introduzca la coordenada y del centro de la segunda circunferencia: "))
r2 = float(input("Introduzca el radio de la segunda circunferencia: "))

distancia = math.sqrt(((x2-x1)**2)+((y2-y1)**2))

if distancia>r1+r2:
    print("\nLas circunferencias son EXTERIORES.")
elif distancia==r1+r2:
    print("\nLas circunferencias son TANGENTES EXTERIORES.")
elif abs(r1-r2)<distancia<r1+r2:
    print("\nLas circunferencias son SECANTES.")
elif distancia==abs(r1-r2):
    print("\nLas circunferencias son TANGENTES INTERIORES.")
elif distancia<abs(r1-r2) and (x1!=x2 or y1!=y2):
    print("\nLas circunferencias son INTERIORES.")
else:
    #x1==x2 and y1==y2
    print("\nLas circunferencias son CONCÉNTRICAS.")
