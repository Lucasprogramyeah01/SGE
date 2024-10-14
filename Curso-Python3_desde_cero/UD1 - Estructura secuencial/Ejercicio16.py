# Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados
# por una distancia d.
# El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo
# para ingresar la distancia entre los dos vehículos (km) y sus respectivas
# velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos)
# alcanzará el vehículo más rápido al otro.

v1 = float(input("Introduzca la velocidad a la que viaja el primer vehículo (km/h): "))
v2 = float(input("Introduzca la velocidad a la que viaja el segundo vehículo (km/h): "))
d = float(input("Introduzca la distancia que separa ambos vehículos: "))

tiempo = d/(v1-v2)

tiempo *= 60

print("Los vehículos coincidarán en %.2f minutos." %(tiempo))
