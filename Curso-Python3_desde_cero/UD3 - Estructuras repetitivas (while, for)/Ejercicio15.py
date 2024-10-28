# Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10
# euros, el segundo 20 euros, el tercero 40 euros y así sucesivamente.
# Realizar un algoritmo para determinar cuánto debe pagar mensualmente y el total
# de lo que pagó después de los 20 meses.

pago = 10
total = 0

i=1
for let in range(i, 20):
    pago *= 2

    total += pago

    print("Durante el mes",i,"el usuario pagó",pago,"€.")

print("\nEl usuario pagó en total",total,"€.")