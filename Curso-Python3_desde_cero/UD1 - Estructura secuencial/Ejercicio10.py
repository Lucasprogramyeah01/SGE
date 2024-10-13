# Un alumno desea saber cual será su calificación final en la materia de Algoritmos
# Dicha calificación se compone de los siguientes porcentajes:
# * 55% del promedio de sus tres calificaciones parciales.
# * 30% de la calificación del examen final.
# * 15% de la calificación de un trabajo final.

parcial1 = float(input("Introduzca su calificación obtenida en el primer parcial: "))
parcial2 = float(input("Introduzca su calificación obtenida en el segundo parcial: "))
parcial3 = float(input("Introduzca su calificación obtenida en el tercer parcial: "))

mediaParciales = (parcial1+parcial2+parcial3)/3

examenFinal = float(input("Introduzca su calificación obtenida en el examen final: "))

trabajoFinal = float(input("Introduzca su calificación obtenida en el trabajo final: "))

calFinal = ((mediaParciales*55)/100)+((examenFinal*30)/100)+((trabajoFinal*15)/100)

print("\nSu calificación final es de: %.2f." %(calFinal))
