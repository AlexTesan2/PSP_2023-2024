"""
Ejercicio 14: Realiza un programa en Python en el que muestres un menú que te permita 3 opciones:
    - 1. Volcado (escritura) de una lista con todos los números pares comprendidos entre 0 y 100.
    - 2. Mostrar (lectura) por pantalla el contenido del fichero de texto creado.
    - 3. Salir del Programa.
"""

def escribirNumPares():
    with open("numerosPares.txt", "w") as archivo:
        for numero in range(0, 101, 2):
            archivo.write(f"{numero}\n")

def mostrarContenido():
    try:
        with open("numerosPares.txt", "r") as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print("El archivo no existe. Primero debes realizar la opción 1.")

while True:
    print("Menú:")
    print("1. Volcado (escritura) de números pares entre 0 y 100.")
    print("2. Mostrar contenido del archivo.")
    print("3. Salir del programa.")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        escribirNumPares()
        print("Números pares han sido escritos en el archivo.")
    elif opcion == "2":
        mostrarContenido()
    elif opcion == "3":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")