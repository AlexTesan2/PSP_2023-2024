import threading
import queue
import time

def trabajador(nombre, cola):
    while True:
        mensaje = cola.get()
        if mensaje == 'FIN':
            break
        print(f'{nombre} dice: {mensaje}')
        #time.sleep(1)

# Crear una cola, sera comun para todos los hilos
mi_cola = queue.Queue()

# Crear dos hilos trabajadores
hilo1 = threading.Thread(target=trabajador, args=('Hilo 1', mi_cola))
hilo2 = threading.Thread(target=trabajador, args=('Hilo 2', mi_cola))

# Iniciar los hilos
hilo1.start()
hilo2.start()

# Encolar algunos mensajes
mi_cola.put('Hola')
mi_cola.put('Cómo estás')
mi_cola.put('Espero que bien')
mi_cola.put('FIN')  # Señal de finalización para cada hilo

# Esperar a que ambos hilos terminen
hilo1.join()
hilo2.join()

print("Programa principal finalizado.")
