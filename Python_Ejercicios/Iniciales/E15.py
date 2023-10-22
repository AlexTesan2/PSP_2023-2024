"""
Ejercicio 15: Crea un fichero de texto con el nombre y contenido que tú desees. Por ejemplo, 
Ejercicio15.txt. Realiza un programa en Python que lea el fichero <<Ejercicio15.txt>> y muestre 
su contenido por pantalla sin espacios. Por ejemplo, si el fichero contiene el siguiente texto 
“Hola que haces”, deberá mostrar “Holaquehaces”.
"""

try:
    with open("Ejercicio15.txt", "r") as archivo:
        contenido = archivo.read()
        contenidoSinEspacios = contenido.replace(" ", "")
        print(contenidoSinEspacios)
except FileNotFoundError:
    print("El archivo no existe.")