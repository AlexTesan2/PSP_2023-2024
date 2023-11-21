"""
Implementa en python un código de Productor Consumidor mediante cola sincronizada tal que:

-El productor produce números enteros mayor que 10 y menor que 1000, el productor 
produce 10 números cada vez que los almacena en la cola y el tiempo de espera entre
la generación de un número y otro es de PT segundos (1 punto)

-El consumidor lee X números de la cola de golpe, calcula el MCD de esos X números .(1,5 punto)


el tiempo de espera entre la lectura de X elementos cola y la siguiente lectura de los 
siguientes X elementos es de  CT segundos (1 punto)
Prueba el algoritmo con los distintos casos usando una relación de productor:consumidor de     
1:1   con PT=1  CT=4 y X=3 (0,5 puntos)
4:2 con PT=2  CT=4 y X=2 (0,5 puntos)
2:10 con PT=1  CT=10 y X=4 (0,5 puntos)
NOTA DAR UN PEQUEÑO TIEMPO ENTRE EL START DE CADA CONSUMIDOR Y/O PRODUCTOR Y EL SIGUIENTE
PARA PODER VER BIEN LOS MENSAJES DEL PRINT
"""


import queue
import threading
import time
import math
import random

class Productor(threading.Thread):
    def __init__(self, cola, PT, cantidad):
        super(Productor, self).__init__()
        self.cola = cola
        self.PT = PT
        self.cantidad = cantidad

    def run(self):
        for _ in range(self.cantidad):
            numero = random.randint(11, 999)
            self.cola.put(numero)
            print(f"Productor produjo: {numero}")
            time.sleep(self.PT)

class Consumidor(threading.Thread):
    def __init__(self, cola, CT, X):
        super(Consumidor, self).__init__()
        self.cola = cola
        self.CT = CT
        self.X = X

    def run(self):
        while True:
            time.sleep(self.CT)
            numeros = []
            for _ in range(self.X):
                numero = self.cola.get()
                numeros.append(numero)
            mcd = self.calcular_mcd(numeros)
            print(f"Consumidor leyó {self.X} elementos: {numeros}, MCD: {mcd}")

    def calcular_mcd(self, numeros):
        if len(numeros) > 1:
            a = numeros[0]
            b = numeros[1]
            mcd_ab = math.gcd(a, b)
            for i in range(2, len(numeros)):
                mcd_ab = math.gcd(mcd_ab, numeros[i])
            return mcd_ab
        elif len(numeros) == 1:
            return numeros[0]
        else:
            return None

if __name__ == "__main__":
    cola = queue.Queue()

    # Configuración de casos de prueba
    casos_prueba = [
        {"productores": 1, "consumidores": 1, "PT": 1, "CT": 4, "X": 3},
        {"productores": 4, "consumidores": 2, "PT": 2, "CT": 4, "X": 2},
        {"productores": 2, "consumidores": 10, "PT": 1, "CT": 10, "X": 4}
    ]

    for caso in casos_prueba:
        print(f"\n----- Caso de prueba: {caso} -----")

        # Crear productores y consumidores según la configuración
        productores = [Productor(cola, caso["PT"], 10) for _ in range(caso["productores"])]
        consumidores = [Consumidor(cola, caso["CT"], caso["X"]) for _ in range(caso["consumidores"])]

        # Iniciar productores y consumidores
        for p in productores:
            p.start()
            time.sleep(0.5)  # Pequeño tiempo entre el inicio de cada productor
        for c in consumidores:
            c.start()
            time.sleep(0.5)  # Pequeño tiempo entre el inicio de cada consumidor

        # Esperar a que todos los productores y consumidores terminen
        for p in productores:
            p.join()
        for c in consumidores:
            c.join()
