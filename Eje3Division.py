# División de cadenas
def dividir_cadena(cadena,delimitador):
    ok = cadena.split(sep = delimitador)
    print(ok)

#programa principal
texto = input("ingresa una cadena de texto: ")
deli = input("ingrese un caracter delimitador: ")
dividir_cadena(texto,deli)