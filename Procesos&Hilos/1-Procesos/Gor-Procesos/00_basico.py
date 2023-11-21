import multiprocessing

def tarea_proceso(nombre):
    print(f'Hola, {nombre}!')

if __name__ == '__main__':
    # Crear un objeto de proceso
    proceso = multiprocessing.Process(target=tarea_proceso, args=('Mundo',))

    # Iniciar el proceso
    proceso.start()

    # Esperar a que el proceso termine
    proceso.join()

    print('Proceso principal ha terminado.')