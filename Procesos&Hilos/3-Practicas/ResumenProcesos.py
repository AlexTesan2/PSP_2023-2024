import multiprocessing
import Lock
import os
import psutil
import time

def funcion():
    pass
if __name__ == '__main__':
    proceso = multiprocessing.Process(target=funcion, args=())

# Iniciar y terminar procesos
proceso.start()
proceso.join()

#colas
cola = multiprocessing.Queue()
cola.put(1)                                 #meter en cola
cola.get()                                  #sacar de cola

#bloqueador
lock = Lock()
lock.acquire()
lock.release()

#grupo de 7 procesos
pool = multiprocessing.Pool(7)
pool.map(funcion, range(10))                #en el mismo orden en el que se dan los datos
pool.imap_unordered(funcion, range(10))     #orden arbitrario
res = pool.apply_async(funcion, (20,))      #llamada asíncrona
print (res.get(timeout=1))
pool.starmap(funcion, [(num,) for num in range(10) ])

#Hijos
hijo = os.fork()
if hijo == 0:       #Este código solo se ejecuta en el proceso hijo
    pass
os.getpid()         #Id proceso
os.getppid()        #Id proceso padre
#os._exit(0)        #mata proceso hijo

#psutil
proceso.name()      #nombre
proceso.pid         #Id proceso
proceso.cwd()       #ruta directorio
proceso.nice()      #prioridad
proceso.username()  #nombre de usuario
proceso.status()    #estado
for proc in psutil.process_iter():    # Itera sobre todos los procesos en ejecución.
    pass
proc.kill()         #Elimina el proceso

#tiempo
time.sleep(2)