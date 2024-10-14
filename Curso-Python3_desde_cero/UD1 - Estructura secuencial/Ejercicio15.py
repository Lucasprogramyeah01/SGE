# Dadas dos variables numéricas A y B, que el usuario debe teclear,
# se pide realizar un algoritmo que intercambie los valores de ambas variables
# y muestre cuanto valen al final las dos variables.

a = int(input("Introduce el valor de la variable A: "))
b = int(input("Introduce el valor de la variable B: "))
aux = a
a = b
b = aux
print("El nuevo valor de A es:", a)
print("El nuevo valor de B es:", b)