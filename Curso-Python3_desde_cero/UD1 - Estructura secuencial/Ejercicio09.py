# Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente
# desea saber cuanto deberá pagar finalmente por su compra.

precioBase = float(input("Introduzca el precio base de la compra realizada: "))

descuento = precioBase - ((precioBase*15)/100)

print("El precio final de la compra sería de %.2f €." %(descuento))
