import math

#EJERCICIO 1 --------------------------------------------------------------------------------------

base = 15
altura = 10

def area_rectangulo(base, altura) :
    return base*altura

print("El área del rectángulo es de: ", area_rectangulo(base, altura), " m^2.")

#EJERCICIO 2 --------------------------------------------------------------------------------------

radio = 5

def area_circulo(radio) :
    return math.pi*(radio)**2

print("El área del círculo es de: ", area_circulo(radio), " m^2.")

#EJERCICIO 3 --------------------------------------------------------------------------------------

a = 5
b = 10

def relacion(a, b) :
    if(a > b):
        return 1
    if(a < b):
        return -1
    else:
        return 0
    
print(relacion(a, b))
print(relacion(b, a))
print(relacion(a, a))

#EJERCICIO 4 --------------------------------------------------------------------------------------

a = -12
b = 24

def intermedio(a, b) :
    return (a+b)/2

print(intermedio(a, b))

#EJERCICIO 5 --------------------------------------------------------------------------------------

numero = 15
minimo = 0
maximo = 10

def recortar(numero, minimo, maximo) :
    if(numero < minimo) :
        return minimo
    if(numero > maximo) :
        return maximo
    else:
        return numero

print(recortar(numero, minimo, maximo))

#EJERCICIO 6 --------------------------------------------------------------------------------------

lista = [3, 6, 7, 4, 1]

pares = []
impares = []

def separar(lista) :
    for i in lista :
        if(i%2 == 0) :
            pares.append(i)
        else :
            impares.append(i)

        pares.sort()
        impares.sort()

    return pares, impares

pares, impares = separar(lista)

print(pares, impares)
