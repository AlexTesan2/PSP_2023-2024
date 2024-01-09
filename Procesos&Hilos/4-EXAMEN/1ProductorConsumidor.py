"""
Implementa en python un código de Productor Consumidor mediante cola sincronizada tal que:

-El productor produce números enteros mayor que 100 y menor que 500(Aleatorios), 
el tiempo de espera entre la generación de un número y otro es de PT segundos (1 punto)

-El consumidor lee X números de la cola de golpe, calcula la multiplicación 
de esos X números .(1 punto).el tiempo de espera entre la lectura de X elementos cola y
la siguiente lectura de los siguientes X elementos es de  CT segundos (1 punto)

Prueba el algoritmo con los distintos casos usando una relación de productor:consumidor de     
1:1 con PT=1  CT=4 y X=3 (0,5 puntos)
4:2 con PT=2  CT=2 y X=2 (0,5 puntos)
2:6 con PT=1  CT=10 y X=4 (0,5 puntos)

"""

import threading 
import time 
import queue 
import random

class Productor(threading.Thread): 
    def __init__(self, queue, PT): 
        threading.Thread.__init__(self)
        self.queue = queue 
        self.PT=PT

    def run(self):
        while True:
            numeroNew= random.randint(101, 500)
            self.queue.put(numeroNew)
            print(f"{numeroNew} añadido a la cola          ++++")
            time.sleep(self.PT)

class Consumidor(threading.Thread): 
    def __init__(self, queue, CT, X): 
        threading.Thread.__init__(self)
        self.queue = queue 
        self.CT=CT
        self.X=X
    
    def run(self):
        while True:
            multiplicacion=1
            for i in range (self.X):
                if not self.queue.empty():
                    numero=self.queue.get()
                    multiplicacion=multiplicacion*numero
                    print(f"{numero} eliminado de la cola   ---")
                else:
                    i=i-1
            print(f"la multiplicacion de los {self.X} numeros es {multiplicacion}")
            time.sleep(self.CT)


def arrancar(NP, NC, PT, CT, X):
    cola = queue.Queue()
    hilosP = []
    hilosC = []

    for i in range (NP):
        productor=Productor(cola,PT)
        hilosP.append(productor)
        productor.start()

    for i in range (NC):
        consumidor=Consumidor(cola,CT,X)
        hilosC.append(consumidor)
        consumidor.start()
    
    for p in hilosP:
        p.join()
    print("\n productores cerrados")
    for c in hilosC:
        c.join()
    print("consumidores cerrados")





def posible_1():
    NP=1    #num productor
    NC=1    #num consumidor
    PT=1    #tiempo espera productor
    CT=4    #tiempo espera consumidor
    X =3    #num elementos leídos por el consumidor de golpe
    return(NP,NC,PT,CT,X)

def posible_2():
    NP=4
    NC=2
    PT=2
    CT=2
    X =2
    return(NP,NC,PT,CT,X)

def posible_3():
    NP=2
    NC=6
    PT=1
    CT=10
    X =4
    return(NP,NC,PT,CT,X)

if __name__ == '__main__':
    NP, NC, PT, CT, X = posible_1()
    #NP, NC, PT, CT, X = posible_2()
    #NP, NC, PT, CT, X = posible_3()
    arrancar(NP, NC, PT, CT, X)