"""Ejercicio 5:  Implementa un programa Python que solicite al usuario una cadena de caracteres 
(String) y muestre por pantalla el número de veces que aparece la sub-cadena “aaa” dentro 
de dicho String."""


frase_usuario = input("Dime algo: ")
veces=0
i = 0

while i < len(frase_usuario):
    if frase_usuario[i:i+3] == "aaa":
        veces += 1
        i += 3
    else:
        i += 1

print (f"La palabra aaa se repite {veces} veces")