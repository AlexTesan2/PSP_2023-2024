from multiprocessing import Process, Lock

def funcion(bloqueador, num):
    
    bloqueador.acquire()        #lock se inicia
    print ('hello world', num)
    bloqueador.release()        #lock se cierra

if __name__ == '__main__':
    lock = Lock()   #no perite que dos procesos realicen la misma tarea a la vez, ht q el primero no termine, no puede empezar el segundo

    for num in range(10):
        Process(target=funcion, args=(lock, num)).start()

#Lock : Para asegurarse de que solo un proceso pueda ejecutar la sección crítica del código a la vez.











"""
def funcion(num):
    print ('hello world', num)

if __name__ == '__main__':
    for num in range(100):
        Process(target=funcion, args=(num,)).start()
"""