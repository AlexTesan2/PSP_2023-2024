"""Escribe un programa Python que pregunte al usuario por 10 números enteros y muestre 
por pantalla el número total de veces que el usuario ha introducido el 0, el número total
de enteros mayores que 0 introducidos y el número total de enteros menores que 0 introducidos."""

VecesIgual__0 = 0
VecesMayor__0 = 0
VecesMenor__0 = 0
contador=0

for i in range(10):
    numero = int(input('('+str(contador+1)+")Ingrese un número entero: "))
    contador=contador+1

    if numero > 0:
        VecesMayor__0 += 1
    elif numero < 0:
        VecesMenor__0 += 1
    else:
        VecesIgual__0 += 1

print("\nTotal de números mayores que 0:", VecesMayor__0)
print("Total de números menores que 0:", VecesMenor__0)
print("Total de números iguales a 0:", VecesIgual__0)