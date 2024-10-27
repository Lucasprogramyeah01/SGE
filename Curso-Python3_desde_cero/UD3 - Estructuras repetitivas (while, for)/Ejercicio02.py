# Crea una aplicación que permita adivinar un número. La aplicación genera un
# número aleatorio del 1 al 100. A continuación va pidiendo números y va
# respondiendo si el número a adivinar es mayor o menor que el introducido,
# además de los intentos que te quedan (tienes 10 intentos para acertarlo).
# El programa termina cuando se acierta el número (además te dice en cuantos
# intentos lo has acertado), si se llega al limite de intentos te muestra el
# número que había generado.

import random

numAleatorio = random.randint(1, 100)

print("\n*********************************************************\n"
      "¡ADIVINA EL NÚMERO ALEATORIO ENTRE 1 Y 100!\n"
      "¿Serás capaz de adivinar cuál es el número misterioso?\n"
      "Dispones de 10 intentos ¡Buena suerte!\n"
      "*********************************************************")

max = 10
for i in range (max, 0, -1):
    numUsuario = int(input("\nIntroduzca el número que crea correcto:"))

    if numUsuario!=numAleatorio:
        max -= 1

        if numUsuario>numAleatorio:
            print("El número a adivinar es menor a", numUsuario,".")
            print("TE QUEDAN",max,"INTENTOS.")
        else:
            print("El número a adivinar es mayor a", numUsuario, ".")
            print("TE QUEDAN", max, "INTENTOS.")

    else:
        print("\n****************************************************\n"
              "¡CORRECTO, EL NÚMERO A ADIVINAR ERA",numAleatorio,"!\n"
              "Has acertado en",10-max,"intentos.\n"
              "****************************************************")
        break;

if max==0:
    print("\n----------------------------------------------------\n"
          "¡Ohhh, el número a adivinar era",numAleatorio,"!\n"
          "La próxima vez será.\n"
          "----------------------------------------------------")