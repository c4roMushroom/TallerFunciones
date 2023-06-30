#1. La función debe devolver la cadena original pero con todas las ocurrencias del caracter a 
#buscar reemplazadas por el caracter de reemplazo.

def reemplazar_cadena(cadena,caracterB, caracterR):
    cadenaz = cadena.replace(caracterB,caracterR)
    print(cadenaz)
    
#programa principal

cadena1 = input("ingrese una cadena de texto: ")
caracterB1 = input("ingrese el caracter que quiere buscar: ")
caracterR1 = input("ingrese el caracter con que quiere reemplazar: ")
reemplazar_cadena(cadena1,caracterB1,caracterR1)