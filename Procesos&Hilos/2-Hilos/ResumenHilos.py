import threading
import queue
import logging

def funcion():
    global g
    pass

class clase(threading.Thread): 
    def __init__(self, queue): 
        threading.Thread.__init__(self)
        self._queue = queue 
    def run(self):
        pass

if __name__ == '__main__':
    hilo = threading.Thread(target=funcion)
    clase(1)
    hilo.start()
    hilo.join()

#colas
mi_cola = queue.Queue()
mi_cola.put('Hola')
mi_cola.get()

#lock
lock = threading.Lock()

#listas
ListaTrabajadores = []
for n in range(5):
    miTrabajador = clase(mi_cola)
    miTrabajador.name = "miHilo"+str (n)
    miTrabajador.start() 
    miTrabajador.append(ListaTrabajadores)

if (threading.current_thread().name == "miHilo2"):
    pass

threading.active_count()
threading.enumerate()
