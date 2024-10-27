# Algoritmo que pida caracteres e imprima 'VOCAL' si son vocales y 'NO VOCAL'
# en caso contrario, el programa termina cuando se introduce un espacio.

caracter = ''

while caracter!=' ':
    caracter = input("Introduzca un caracter: ")

    if(caracter.upper()=='A' or caracter.upper()=='E'
       or caracter.upper()=='I' or caracter.upper()=='O'
       or caracter.upper()=='U'):

        print("VOCAL\n")

    elif(caracter!=' '):
        print("NO VOCAL\n")