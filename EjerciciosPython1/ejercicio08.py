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
    return int(p - (p * (descuentoBien/100)))

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

input("""
*********************************************************
TURNO DEL ESTRATEGA DEL BIEN (JUGADOR 1)
*********************************************************
(>)
""")

try:
    b1 = int(input("GANDALF: Muy bien, es hora de que nos guíes, golpea mi bastón las veces que quieras..."))
    dineroBien = calcularDinero(b1)
    print(f"HAS OBTENIDO: {dineroBien} €.")
except:
    print("Te caes intentando dar el golpe...")
    dineroBien = calcularDinero(1)
    print(f"HAS OBTENIDO: {dineroBien} €.")

try:
    b2 = int(input("\nGANDALF: Y ahora grita ¡POR LAS RAZAS BONDADOSAS! las veces que creas..."))
    descuentoBien = (calcularDescuento(b2))
    print(f"HAS OBTENIDO UN DESCUENTO DEL: {descuentoBien} %.")
except:
    print("Te ahogas intentando gritar y terminas tosiendo...")
    descuentoBien = (calcularDescuento(1))
    print(f"HAS OBTENIDO UN DESCUENTO DEL: {descuentoBien} %.")

input("(>)")

precioPelosoFinal = aplicarDescuento(precioPeloso, descuentoBien)
precioSurenhoBuenoFinal = aplicarDescuento(precioSurenhoBueno, descuentoBien)
precioEnanoFinal = aplicarDescuento(precioEnano, descuentoBien)
precioNumenoreanoFinal = aplicarDescuento(precioNumenoreano, descuentoBien)
precioElfoFinal = aplicarDescuento(precioElfo, descuentoBien)

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

while dineroBien >= precioPelosoFinal:

    try:
        tropaElegida = int(input())
    except:
        tropaElegida = 1
        print(f"Resultas inentendible... Contratas a un Peloso por error...")

    if tropaElegida == 1 and dineroBien >= precioPelosoFinal:
        puntuacionEjercitoBien += 1
        dineroBien -= precioPelosoFinal
        print(f"Has contratado a un Peloso.")
    elif tropaElegida == 2 and dineroBien >= precioSurenhoBuenoFinal:
        puntuacionEjercitoBien += 2
        dineroBien -= precioSurenhoBuenoFinal
        print(f"Has contratado a un Sureño bueno.")
    elif tropaElegida == 3 and dineroBien >= precioEnanoFinal:
            puntuacionEjercitoBien += 3
            dineroBien -= precioEnanoFinal
            print(f"Has contratado a un Enano.")
    elif tropaElegida == 4 and dineroBien >= precioNumenoreanoFinal:
            puntuacionEjercitoBien += 4
            dineroBien -= precioNumenoreanoFinal
            print(f"Has contratado a un Númenoreano.")
    elif tropaElegida == 5 and dineroBien >= precioElfoFinal:
            puntuacionEjercitoBien += 5
            dineroBien -= precioElfoFinal
            print(f"Has contratado a un Elfo.")
    elif tropaElegida == 5 and dineroBien >= precioElfoFinal:
            puntuacionEjercitoBien += 5
            dineroBien -= precioElfoFinal
            print(f"Has contratado a un Elfo.")
    else:
        puntuacionEjercitoBien += 1
        dineroBien -= precioPelosoFinal
        print(f"No hay ninguna tropa con ese número asignado... A cambio, contratas a un Peloso.")
        print(f"Has contratado a un Peloso.")
    
    print(f"Dinero restante: {dineroBien} €.\n")

print(puntuacionEjercitoBien)
         




    













