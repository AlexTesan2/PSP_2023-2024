"""Ejercicio 3: Enumera todos los procesos en el sistema operativo con su PID 
y permite la terminación de uno mediante su PID."""

import psutil

def listar_procesos():
    print("Listado de procesos:")
    print("PID\tNombre del Proceso")

    for proc in psutil.process_iter():
        processName = proc.name()
        processID = proc.pid
        print(f"{processName}\t{processID}")

def terminar_proceso(pid):
    try:
        proceso = psutil.Process(pid)
        proceso.kill()
        print(f"Proceso con PID {pid} terminado exitosamente.")
    except psutil.NoSuchProcess:
        print(f"No existe un proceso con el PID {pid}.")
    except psutil.AccessDenied:
        print(f"No tienes permisos para terminar el proceso con PID {pid}.")


def main():
    listar_procesos()
    pid_a_terminar = int(input("Ingrese el PID del proceso a terminar (0 para salir): "))
    if pid_a_terminar == 0:
        print("Saliendo del programa.")
    else:
        terminar_proceso(pid_a_terminar)

if __name__ == "__main__":
    main()