"""
Ejercicio 2: Utilizando el módulo multiprocessing, escribe un programa simple en Python de la siguiente manera:

Crea un conjunto de trabajadores para ejecutar tareas en paralelo.
El tamaño del conjunto debería ser 2.
Escribe una función para ejecutarse en paralelo, llámala print_cube. La función debería recibir 
como entrada un número [num]. Cuando se llame, la función imprimirá en la pantalla un mensaje 
en la forma: "El cubo del número [num] es [cube]". Donde [cube] deberá ser reemplazado con el 
cubo del número recibido como entrada.
Escribe otra función para ejecutarse en paralelo, llámala print_square. La función debería 
recibir como entrada un número [num]. Cuando se llame, la función imprimirá en la pantalla un 
mensaje en la forma: "El cuadrado del número [num] es [square]". Donde [square] deberá ser 
reemplazado con el cuadrado del número recibido como entrada.
"""

import multiprocessing

def print_cube(num):
    cube=num**3
    print(f"El cubo del número {num} es {cube}")

def print_square(num):
    square=num**2
    print(f"El cuadrado del número {num} es {square}")

def main():
    numeros = [1, 2, 4, 6, 8]# Números de entrada para las funciones

    # Crear un conjunto de trabajadores
    with multiprocessing.Pool(processes=2) as pool:
        # Ejecutar las funciones en paralelo
        pool.starmap(print_cube,   [(num,) for num in numeros])
        pool.starmap(print_square, [(num,) for num in numeros])

if __name__ == "__main__":
    main()