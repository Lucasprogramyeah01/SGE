# Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos)
# después de pedirnos cuantas monedas tenemos de 2€, 1€, 50 céntimos, 20 céntimos
# o 10 céntimos).

monedas1E = int(input("Introduzca la cantidad de monedas de 1€ que posee: "))
monedas2E = int(input("Introduzca la cantidad de monedas de 2€ que posee: "))
monedas10cent = int(input("Introduzca la cantidad de monedas de 10 céntimos que posee: "))
monedas20cent = int(input("Introduzca la cantidad de monedas de 20 céntimos que posee: "))
monedas50cent = int(input("Introduzca la cantidad de monedas de 50 céntimos que posee: "))

totalEnEuros = monedas1E+(monedas2E*2)+(monedas10cent*0.1)+(monedas20cent*0.2)+(monedas50cent*0.5)

totalEnCentimos = (monedas1E*100)+(monedas2E*200)+monedas10cent+(monedas20cent*2)+(monedas50cent*5)

print("\nUsted posee la cantidad de: %.2f € / %.2f céntimos." %(totalEnEuros, totalEnCentimos))