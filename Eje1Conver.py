#1.Implementa una función llamada convertir_mayusculas(cadena) que reciba una cadena de texto como
#argumento y devuelva la misma cadena pero con todos los caracteres en mayúsculas.

def convertir_mayusculas(cadena):
    cadenaM = cadena.upper()
    print(cadenaM)

print("programa de conversion a mayusculas_______________")
texto = input("ingrese una cadena de texto: ")
convertir_mayusculas(texto)

#2. Implementa una función llamada convertir_minusculas(cadena)

def convertir_minusculas(cadena):
    cadenaM = cadena.lower()
    print(cadenaM)

print("programa de conversion a mayusculas_______________")
texto = input("ingrese una cadena de texto: ")
convertir_mayusculas(texto)

#3.En el programa principal, pide al usuario que ingrese una cadena de texto. Luego, llama a las 
#funciones convertir_mayusculas y convertir_minusculas con esa cadena como argumento.

#programa principal
textoT = input("ingrese una cadena de texto: ")
print("mayusculas: ")
convertir_mayusculas(textoT)
print("minusculas: ")
convertir_minusculas(textoT)