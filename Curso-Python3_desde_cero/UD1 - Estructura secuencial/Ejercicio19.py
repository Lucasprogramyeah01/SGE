# Escribir un algoritmo para calcular la nota final de un estudiante, considerando que:
# por cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en
# blanco 0. Imprime el resultado obtenido por el estudiante.

aciertos = int(input("Introduzca su número de respuestas correctas: "))
fallos = int(input("Introduzca su número de respuestas incorrectas: "))
enBlanco = int(input("Introduzca su número de respuestas dejadas en blanco: "))

numPreguntas = aciertos+fallos+enBlanco

puntuacion = (aciertos*5)-fallos

print("\nSu puntación es de:",puntuacion,"sobre",numPreguntas*5,".")

