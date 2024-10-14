# Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

nombre = input("Introduzca su nombre: ")
apellido1 = input("Introduzca su primer apellido: ")
apellido2 = input("Introduzca su segundo apellido: ")

iniciales = nombre[0]+apellido1[0]+apellido2[0]

print("Sus iniciales son:",iniciales,".")