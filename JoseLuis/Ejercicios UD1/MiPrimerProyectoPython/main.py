print("Hola mundo")

#ARITMETICA

print(2+3)
print(2-3)
print(2*3)
print(2/3)
print(2**3)
print(2%3)

#VARIABLES

res = None  #None es como null en Java.
res = 3
res = "Hola"

print(res)

#CADENAS
#Las cadenas se pueden escribir tanto con comillas simples como dobles.

cadena = "Me llamaban 'Aitor'"
cadena = 'Me llamaban "Aitor"'

#FUNCIONES

def nombre_funcion(parametro1):
    res="Jose Luis"
    res="David"
    return res

print (len("Hola mundo"))

res = []

for i in range(10):
    res.append(i)

print(res)

res2=["Cadena", 7, 3.14, True, False, res]

print(res2)

#LISTAS

datos = [4, "Una cadena", True]

pares = [0, 2, 4, 5]

#lpares[:3] - []

#MATRICES

a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
r = [a, b, c]

print(r)

print(r[0][2]) #Esta sentencia imprimiría por pantalla el último elemento de la primera lista de la matriz.

#-------------------------------------------------------------------------------------------------------------------------------------------------------------

#INTRODUCIR DATOS POR TECLADO

nombre = input("¿Cuál es tu nombre?")

print("Hola", nombre, "¿Cómo estás?")

#OPERADORES LÓGICOS

1 + 1 == 3 #Devuelve True
3 != 3 #Devuelve False

# "&&" para "AND", "||" para "OR".

#OPERADERES DE ASIGNACION

x = 2

x += 4 #Devolvería 6 si imprimiera por pantalla. 

#-------------------------------------------------------------------------------------------------------------------------------------------------------------

#BUCLES

f = 0
while f <= 5:
    f+=1
    print("f vale", f)

listaNum = [1, 2, 3, 4, 5]
for numero in listaNum:
    listaNum *= 10
listaNum

listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for indice, numero in enumerate(listaNumeros):
    listaNumeros[indice] *= 10
listaNumeros

#TUPLAS

tupla = (100, "Hola", [1,2,3], -50) #Una tupla es una forma de almacenar datos.

#MÉTODO .index (Muestra en qué índice se encuentra un dato).

tupla.index(100)

#MÉTODO .count (Muestra cuantas veces se repite un elemento en la tupla).

tupla.count(100)

#CONJUNTOS

conjunto = {1, 2, 3}

conjuntoVacio = set.set()

#DICCIONARIOS (Map en Java)

colores = {1:"Rojo", 2:"Naranja", 3:"Amarillo"} #Clave:Valor

#PILAS (El último en entrar es el primero en salir). Método pop

#COLAS (El primero en entrar es el primero en salir). Método porleft()