# Realiza un algoritmo que calcule la potencia, para ello pide por teclado
# la base y el exponente. Pueden ocurrir tres cosas:
#  * El exponente sea positivo, sólo tienes que imprimir la potencia.
#  * El exponente sea 0, el resultado es 1.
#  * El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

base = float(input("Introduzca la base de la potencia: "))
exponente = float(input("Introduzca el exponente de la potencia: "))

if exponente>0:
    potencia = base**exponente
    print("\nLa potencia de %.2f elevado a %.2f es: %.2f." %(base, exponente, potencia))
elif exponente < 0:
    potencia = 1/(base**(-exponente))
    print("\nLa potencia de %.2f elevado a %.2f es: %.2f." % (base, exponente, potencia))
else:
    print("\nLa potencia de %.2f elevado a %.2f es: 1." % (base, exponente))
    print("(Todo número elevado a 0 es 1).")

