# Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas,
# el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por
# las tres ventas que realiza en el mes y el total que recibirá en el mes tomando
# en cuenta su sueldo base y comisiones.

sueldoBase = float(input("Introduzca su sueldo base: "))

venta1 = float(input("Introduzca el dinero obtenido en la primera venta: "))
venta2 = float(input("Introduzca el dinero obtenido en la segunda venta: "))
venta3 = float(input("Introduzca el dinero obtenido en la tercera venta: "))

comision = (venta1*0.1)+(venta2*0.1)+(venta3*0.1)

print("\nLa comisión por ventas sería de: %.2f €." %(comision))
print("Su sueldo total sería de: %.2f €." %(sueldoBase+comision))
