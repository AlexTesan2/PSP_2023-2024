"""Ejercicio 3:  ¡IMPLEMENTA TU PRIMER JUEGO! Realiza un programa Python que adivine el número.
El programa generará un número aleatorio entre 0 y 20 y luego irá pidiendo números al usuario 
indicando “mayor” o “menor” según sea mayor o menor con respecto al número generado aleatoriamente. 
El proceso termina cuando el usuario acierta, y deberá mostrar un mensaje de felicitaciones junto
al número de intentos que ha necesitado el usuario."""

import random

numero_intentos = 0
numero_imaginado = random.randint(0,20)
intento= 0

frase_Inicial = "\nTe propongo un JUEGO, me invento un NUMERO y tu lo tines que ADIVINAR \n"
felicitaciones = "Felicidades, has adivinado el acertijo, y solo te ha costado "
frIntenta = "Prueba con un numero: "
mayor = "Casi, pero el numero que he pensado es mayor "
menor = "estas cerca, pero el numero que he pensado es menor "

print(frase_Inicial)
intento=int(input(frIntenta))

while intento != numero_imaginado:
    numero_intentos += 1
    if intento < numero_imaginado:
        print(mayor)
    else:
        print(menor)
    intento=int(input(frIntenta))

if intento == numero_imaginado:
    print ("\n"+ felicitaciones + str(numero_intentos)+ " Intentos /("+str(numero_imaginado)+")")