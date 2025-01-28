"""
EJERCICIO 1
---------------------------------------------------------------------------------------------------------
Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
    - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
    - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
    - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.
"""

listaConversion = {
    "A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".", "F":"..-.", "G":"--.",
    "H":"....", "I":"..", "J":".---", "K":"-.-", "L":".-..", "M":"--", "N":"-.",
    "O":"---", "P":".--.", "Q":"--.-", "R":".-.", "S":"...", "T":"-", "U":"..-",
    "V":"...-", "W":".--", "X":"-..-", "Y":"-.--", "Z":"--..",
    "1":".----", "2":"..---", "3":"...--", "4":"....-", "5":".....", "6":"_....",
    "7":"--...", "8":"---..", "9":"----.", "0":"-----", 
    " ":"  " 
}

listaConversionALetras= {v: k for k, v in listaConversion.items()}

def deMorseANatural (mensaje):
    listamensajeConvertido = list()
    palabras = mensaje.split("  ")

    for palabra in palabras:
        letras = palabra.split(" ")
        for letra in letras:
            if letra in listaConversionALetras:
                listamensajeConvertido.append(listaConversionALetras[letra])
        listamensajeConvertido.append(" ")

    return listamensajeConvertido

def deNaturalAMorse (listaSimbolos):
    listamensajeConvertido = list()

    for simbolo in listaSimbolos:
        for conversion in listaConversion:            
            if(simbolo == conversion):
                if(simbolo == " "):
                    listamensajeConvertido.append(" ")
                else:
                    listamensajeConvertido.append(listaConversion.get(simbolo))
                    listamensajeConvertido.append(" ")
    
    return listamensajeConvertido

#---------------------------------------------------------------------------------------------------------------------

mensaje = input("Por favor introduzca su mensaje.\n")

listaSimbolos = list(mensaje.upper())
delimitador = ""

if mensaje.startswith("-") or mensaje.startswith("."):
    print(f"\nMensaje en natural: {delimitador.join(deMorseANatural(mensaje))}")
else:
    print(f"\nMensaje en morse: {delimitador.join(deNaturalAMorse(listaSimbolos))}")
