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

def calcularDinero (x):
    for var in range(x):
        numAleatorio = random.randint(1,8)
    
    return numAleatorio*20

def calcularDescuento (d):
    for var in range(d):
        numAleatorio = random.randint(0,5)
    
    return numAleatorio*10

def aplicarDescuento (p, descuentoBien):
    if(descuentoBien == 0):
        return int(p)
    else:
        return int(p * (descuentoBien/100))

#---------------------------------------------------------------------------------------------------------------------------------------------

puntuacionEjercitoBien = 0
puntuacionEjercitoMal = 0

precioPeloso = 10
precioSurenhoBueno = 20
precioEnano = 30
precioNumenoreano = 40
precioElfo = 50

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
dineroBien = calcularDinero(b1)
print(f"HAS OBTENIDO: {dineroBien} €.")


b2 = int(input("\nGANDALF: Y ahora grita ¡POR LAS RAZAS BONDADOSAS! las veces que creas..."))
descuentoBien = (calcularDescuento(b2))
print(f"HAS OBTENIDO UN DESCUENTO DEL: {descuentoBien} %.")

input("(>)")

precioPelosoFinal = aplicarDescuento(precioPeloso, descuentoBien)
precioSurenhoBuenoFinal = aplicarDescuento(precioSurenhoBueno, descuentoBien)
precioEnanoFinal = aplicarDescuento(precioEnano, descuentoBien)
precioNumenoreanoFinal = aplicarDescuento(precioNumenoreano, descuentoBien)
precioElfoFinal = aplicarDescuento(precioElfo, descuentoBien)

#while dineroBien > 0 :
print(f"""
---------------------------------------------------------
Crea el ejército del BIEN ¡ELIGE TUS TROPAS!
---------------------------------------------------------
DINERO: {dineroBien} €
DESCUENTO: {descuentoBien} %
---------------------------------------------------------
1 ->    {precioPelosoFinal} € - Peloso
2 ->    {precioSurenhoBuenoFinal} € - Sureño bueno
3 ->    {precioEnanoFinal} € - Enano
4 ->    {precioNumenoreanoFinal} € - Númenoreano
5 ->    {precioElfoFinal} € - Elfo
---------------------------------------------------------
          """)

tropaElegida = input()

if tropaElegida == 1:
    puntuacionEjercitoBien += 1
    dineroBien -= precioPelosoFinal
elif tropaElegida == 2:
    puntuacionEjercitoBien += 2
    dineroBien -= precioSurenhoBuenoFinal



    













