"""Ejercicio 1: Implementa un programa Python que PREGUNTE al usuario 
por dos números enteros (x, y) y muestre por pantalla la suma, resta, multiplicación,
división y resto de ambos,con el siguiente formato:
x + y = …
x – y = …
x * y = …
x / y = …
x % y = …"""

x = int(input("Ingrese el primer numero:  "))
y = int(input("Ingrese el segundo numero:  "))

print(str(x) + "+" + str(y) +"=  " + str(x + y))
print(str(x) + "-" + str(y) +"=  " + str(x - y))
print(str(x) + "*" + str(y) +"=  " + str(x * y))

if y==0:
    print ("Infinito")
else:
    print(str(x) + "/" + str(y) +"=  " +str((float)(x/y)))    
    print(str(x) + "%" + str(y) +"=  " +str(x % y))