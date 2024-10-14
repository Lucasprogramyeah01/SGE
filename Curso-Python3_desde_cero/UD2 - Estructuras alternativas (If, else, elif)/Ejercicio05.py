# Escribe un programa que pida un nombre de usuario y una contraseña
# y si se ha introducido "pepe" y "asdasd" se indica "Has entrado al sistema",
# sino se da un error.

nombreUsuario = input("Introduzca un nombre de usuario: ")
contrasenha = input("Introduzca una contraseña: ")

if nombreUsuario=="pepe" and contrasenha=="asdasd":
    print("\nHas accedido al sistema.")
else:
    print("\nERROR: Nombre de usuario o contraseña incorrectos.")