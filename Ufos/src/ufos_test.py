from ufos import *

# Test de la función lee_avistamientos

avistamientos = lee_avistamientos('Ufos\data\ovnis.csv')

for a in avistamientos[:5] :
    print(a)

#Test de la función duracion_total



# Test de la función comentario_mas_largo



# Test de la función avistamientos_fechas

# Llamada a la función
resultado = indexa_formas_por_mes(avistamientos)

# Imprimir el resultado
for mes, formas in resultado.items():
    print(f"{mes}: {formas}")

# Test de la función hora_mas_avistamientos









