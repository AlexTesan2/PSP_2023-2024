"""
solicite al usuario una cadena de caracteres (String) y muestre por pantalla 
dicha cadena, pero con el primer y último carácter cambiados de posición.
"""

frase = input("Dime algo: ")
if len(frase)>1:
    frase = frase[-1]+ frase[1:-1]+ frase[0]
    print(frase)
else :
    print("DAME MAS ")