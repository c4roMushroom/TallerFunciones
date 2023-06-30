#Comprobación de subcadena
def comprobar_subcadena(cadena, subcadena):
    if subcadena in cadena:
        print("True")
    else:
        print("False")

#programa principal
texto = input("ingrese una cadena de texto: ")
sub = input("ingrese una subcadena: ")
comprobar_subcadena(texto,sub)