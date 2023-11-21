import psutil
import os
import time

# Función para imprimir información sobre un proceso
def print_process_info(process):
    print(f"ID del proceso: {process.pid}")
    print(f"Nombre del proceso: {process.name()}")
    print(f"Estado del proceso: {process.status()}")
    print(f"Prioridad del proceso (nice): {process.nice()}")

# Obtener la lista de todos los procesos
all_processes = psutil.process_iter()

# Elegir un proceso específico (por ejemplo, el proceso actual del script)
current_process = psutil.Process(os.getpid())

# Imprimir información sobre el proceso antes de cambiar la prioridad
print("Antes de cambiar la prioridad:")
print_process_info(current_process)

# Cambiar la prioridad del proceso (ajustar el valor nice)
current_process.nice(5)

# Imprimir información sobre el proceso después de cambiar la prioridad
print("\nDespués de cambiar la prioridad:")
print_process_info(current_process)

# Esperar un momento antes de matar el proceso (para que puedas observar los cambios)
time.sleep(2)

# Matar el proceso
current_process.kill()

print("\nProceso terminado.")
