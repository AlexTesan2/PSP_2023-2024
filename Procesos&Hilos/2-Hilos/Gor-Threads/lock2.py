import threading
import time

# Variable compartida entre los hilos
counter = 0

# Crear un objeto de bloqueo
lock = threading.Lock()

def incrementar():
    global counter
    for _ in range(1000000):
        # Adquirir el bloqueo antes de modificar la variable compartida
        lock.acquire()
        try:
            counter += 1
        finally:
            # Liberar el bloqueo
            lock.release()
    
    """
    for _ in range(1000000):
        with lock:
            counter -= 1
    """

def decrementar():
    global counter
    for _ in range(1000000):
        # Adquirir el bloqueo antes de modificar la variable compartida
        lock.acquire()
        try:
            counter -= 1
        finally:
            # Liberar el bloqueo
            lock.release()

if __name__ == '__main__':
    # Crear dos hilos que incrementan y decrementan la variable
    hilo_incrementar = threading.Thread(target=incrementar)
    hilo_decrementar = threading.Thread(target=decrementar)

    # Iniciar los hilos
    hilo_incrementar.start()
    hilo_decrementar.start()

    # Esperar a que ambos hilos terminen
    hilo_incrementar.join()
    hilo_decrementar.join()

    print("Valor final de la variable compartida:", counter)