"""Implementa un programa Python con un método llamado sum(int [] tabla) que muestre por 
pantalla el resultado de sumar todos los elementos de la tabla pasada como parámetro."""

def sum(tabla: list[int]):
    suma = 0
    for i in tabla:
        suma += i
    return suma

numeros = [1, 2, 3, 4, 5]
resultado = sum(numeros)
print(resultado)