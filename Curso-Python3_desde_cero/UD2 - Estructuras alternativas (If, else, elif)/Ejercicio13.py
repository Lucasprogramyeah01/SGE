# Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.

#EJERCICIO SIN ACABAR

dia = int(input("Introduzca un día (en números): "))
mes = int(input("Introduzca un número del mes: "))
anho = int(input("Introduzca un año: "))

if(mes > 0 or mes < 13):
    #if()
    print("La fehca introducida: (", dia, "/", mes, "/", anho, ") es CORRECTA.")
else:
    print("La fehca introducida: (",dia,"/",mes,"/",anho,") es INCORRECTA.")