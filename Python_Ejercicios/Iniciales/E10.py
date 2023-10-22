#Ejercicio 10:  Implementa un método Python llamado mayorYmenor, el cual recibe como parámetro 
# una tabla de Strings y muestra por pantalla el String con mayor longitud y el String con menor longitud.

tabla = ["casa", "castillo", "cadena", "si", "hola","7"]

def mayorYmenor(tabla):
    mayor = tabla[0]
    menor = tabla[0]

    for i in tabla:
        if len(i) > len(mayor):
            mayor = i
        elif len(i) < len(menor):
            menor = i

    print(f"El string con mayor longitud es: '{mayor}' y el string con menor longitud es: '{menor}'")

mayorYmenor(tabla)