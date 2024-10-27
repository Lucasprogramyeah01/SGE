# La asociación de vinicultores tiene como política fijar un precio inicial
# al kilo de uva, la cual se clasifica en tipos A y B,  y además en tamaños 1 y 2.
# Cuando se realiza la venta del producto, ésta es de un solo tipo y tamaño,
#se requiere determinar cuánto recibirá un productor por la uva que entrega en un
#embarque, considerando lo siguiente:
# si es de tipo A, se le cargan 20 céntimos al precio inicial cuando es
# de tamaño 1; y 30 céntimos si es de tamaño 2.
# Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos
# cuando es de tamaño 2.
# Realice un algoritmo para determinar la ganancia obtenida.

precioInicial = float(input("Introduzca el precio inicial por kilo de uva (céntimos): "))
kilos = float(input("Introduzca cuántos kilos de uva desea comprar: "))

tipo = input("\nIntroduzca el tipo de uva que desea comprar (A o B): ")
tamanho = int(input("Introduzca el tamaño de las uvas que desea comprar (1 o 2): "))

if(tipo.upper()=='A' and tamanho==1):
    precioInicial = precioInicial+20
elif(tipo.upper()=='A' and tamanho==2):
    precioInicial = precioInicial+30
elif(tipo.upper()=='B' and tamanho==1):
    precioInicial = precioInicial-20
elif(tipo.upper()=='B' and tamanho==2):
    precioInicial = precioInicial-30

ganancia = (kilos * precioInicial)/100

print("\nLa ganancia obtenida es de %.2f €." %(ganancia))