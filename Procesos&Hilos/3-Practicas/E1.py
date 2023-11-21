"""
Ejercicio 1: Utilizando el módulo multiprocessing, 
escribe un programa simple en Python de la siguiente manera:

Crea un conjunto de trabajadores para ejecutar tareas en paralelo.
El tamaño del conjunto debería ser el número de núcleos de CPU 
disponibles en tu nodo menos 1 (8 núcleos > conjunto de 7 trabajadores).
Escribe una función que se ejecute en paralelo, llámala my_id. 
La función debería recibir como entrada el ID de la tarea. 
Cuando se llame, la función imprimirá en la pantalla un mensaje en
la forma: "Hola, soy el trabajador ID (con PID)", donde ID debería 
ser reemplazado con el número de tarea asignado al trabajador y PID
con el ID de proceso del trabajador en ejecución.
Ejecuta tareas en paralelo utilizando la función map, para un total 
de tareas igual al doble del número de núcleos de CPU en tu nodo.
"""

import multiprocessing
import os

def my_id(task_id):
    # Obtener el ID del proceso en ejecución
    process_id = os.getpid()
    print(f"Hola, soy el trabajador {task_id} (con PID {process_id})")

def main():
    # num de núcleos de CPU disponibles
    num_cores = multiprocessing.cpu_count()
    num_workers = num_cores - 1     # num trabajadores
    total_tasks = 2 * num_cores     # Número total de tareas

    with multiprocessing.Pool(processes=num_workers) as pool:
        # Ejecutar tareas en paralelo utilizando la función map
        pool.map(my_id, range(total_tasks))


if __name__ == "__main__":
    main()