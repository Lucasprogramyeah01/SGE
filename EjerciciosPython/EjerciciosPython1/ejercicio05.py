"""
EJERCICIO 5
---------------------------------------------------------------------------------------------------------
Crea una función que evalúe si un/a atleta ha superado correctamente una carrera de obstáculos.

    - La función recibirá dos parámetros:
        - Un array que sólo puede contener String con las palabras "run" o "jump"
        - Un String que represente la pista y sólo puede contener "_" (suelo) o "|" (valla)

    - La función imprimirá cómo ha finalizado la carrera:
        - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será correcto y no variará 
        - el símbolo de esa parte de la pista.
        - Si hace "jump" en "_" (suelo), se variará la pista por "x".
        - Si hace "run" en "|" (valla), se variará la pista por "/".
    
    - La función retornará un Boolean que indique si ha superado la carrera. Para ello tiene que 
      realizar la opción correcta en cada tramo de la pista.
"""

def evaluarAtleta(listaRecorrido, listaAcciones):
    
    evaluacion = list()
    carreraSuperada = True

    delimitador = " "

    for accion, parte in zip(listaAcciones, listaRecorrido):
        if accion == "run" and parte == "_":
            evaluacion.append("_")
        elif accion == "jump" and parte == "|":
            evaluacion.append("|")
        elif accion == "run" and parte == "|":
            evaluacion.append("/")
            carreraSuperada = False
        else:
            evaluacion.append("x")
            carreraSuperada = False

    if(carreraSuperada):
        return print(f"\nEl atleta ha superado la carrera con éxito ¡YAY! \nMAPA DE LA CARRERA: {delimitador.join(evaluacion)}.")
    else:
        return print(f"\nEl atleta no ha superado la carrera... Ohhh... \nMAPA DE LA CARRERA: {delimitador.join(evaluacion)}")

#---------------------------------------------------------------------------------------------------------------------

pista = input("Introduzca el mapa de la pista de atletismo:\n")
acciones = input("\nIntroduzca las acciones que el corredor ha realizado durante la carrera:\n")

listaRecorrido = pista.lower().split(" ")
listaAcciones = acciones.split(" ")

evaluarAtleta(listaRecorrido, listaAcciones)
