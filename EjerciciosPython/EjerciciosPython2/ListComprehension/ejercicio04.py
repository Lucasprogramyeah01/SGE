"""
EJERCICIO 4
---------------------------------------------------------------------------------------------------------
Crea una lista de todas las consonantes de la cadena: "A los yaks amarillos les gusta gritar y bostezar 
y ayer cantaban mientras comían ñames asquerosos".
"""

# ACLARACIÓN: He realizado este ejercicio de dos formas diferentes porque veía ambas muy claras.

cadena = "A los yaks amarillos les gusta gritar y bostezar y ayer cantaban mientras comían ñames asquerosos"

# PRIMERA FORMA:
listaConsonantes1 = list(c.lower() for c in list(cadena.lower()) if c!="a" and c!="e" and c!="i" and c!="o" and c!="u" and c!=" ")

# SEGUNDA FORMA:
listaConsonantes2 = list(filter(lambda c : c!="a" and c!="e" and c!="i" and c!="o" and c!="u" and c!=" ", list(cadena.lower())))

print(listaConsonantes1)
print(listaConsonantes2)
