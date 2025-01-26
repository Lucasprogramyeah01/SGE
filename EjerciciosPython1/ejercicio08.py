"""
EJERCICIO 8
--------------------------------------------------------------------------------------------------------------
¡La Tierra Media está en guerra! En ella lucharán razas leales a Sauron contra otras bondadosas que no quieren 
que el mal reine sobre sus tierras. Cada raza tiene asociado un "valor" entre 1 y 5:

    - Razas bondadosas: Pelosos (1), Sureños buenos (2), Enanos (3),  Númenoreanos (4), Elfos (5)
    - Razas malvadas: Sureños malos (2), Orcos (2), Goblins (3),  Huargos (4), Trolls (5)

Crea un programa que calcule el resultado de la batalla entre los 2 tipos de ejércitos:

    - El resultado puede ser que gane el bien, el mal, o exista un empate. Dependiendo de la suma del valor 
      del ejército y el número de integrantes.
    - Cada ejército puede estar compuesto por un número de integrantes variable de cada raza.
    - Tienes total libertad para modelar los datos del ejercicio.

Ej: 1 Peloso pierde contra 1 Orco
    2 Pelosos empatan contra 1 Orco
    3 Pelosos ganan a 1 Orco
"""

import random

print("¡LA TIERRA MEDIA ESTÁ EN GUERRA! Y sólo un honorable estratega como tú puede salvarnos...")
print("(Cuando vea este símbolo (>) pulse 'Enter' para seguir con el diálogo.)")
input("(>)")

input("\nGANDALF: Me presento, soy Gandalf, uno de los 5 istari a cargo de combatir a esa peste de Sauron que se cierne"+
      " sobre nosotros. (>)")
input("\nSAURON: Mua ja ja, muy inteligente, Gandalf, pero no creas que va ser cosa fácil ¡Yo también tengo un estratega!"+
      "¡MI PODER ACABARÁ CON VOSOTROS! (>)")

input("\nGANDALF: Me da que va llegando la hora de pegarse... ¡MÁS OS VALE CORRER, INSENSATOS! (>)")
input("\nSAURON: Lo mismo te digo, fósil decrépito. (>)")

print("\n--------------------------------------------------------------------------------------------------------------------------")

b1 = int(input("\nGANDALF: Muy bien, es hora de que nos guíes, golpea mi bastón las veces que quieras..."))
b2 = int(input("\nGANDALF: Y ahora grita ¡POR LAS RAZAS BONDADOSAS! las veces que creas..."))

def calcularDinero (x):

    for var in range(x):
        numAleatorio = random.randint(0,8)
    
    return numAleatorio*10

def calcularDescuento (d):

    for var in range(d):
        numAleatorio = random.randint(0,5)
    
    return numAleatorio*10

while numSoldadosBien

print(calcularDatos(numSoldadosBien))
print(calcularDatos(descuentoBien))


    













