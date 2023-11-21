import threading
import time

def imprimir_numeros():
    for i in range(1, 6):
        time.sleep(1)  # Simula una tarea que toma 1 segundo
        print(f'Número: {i}')

# Crear un hilo
hilo = threading.Thread(target=imprimir_numeros)

# Iniciar el hilo
hilo.start()

# El programa principal puede seguir ejecutándose mientras el hilo está activo
for letra in 'ABCDE':
    time.sleep(0.5)
    print(f'Letra: {letra}')

# Esperar a que el hilo termine antes de que el programa principal finalice
hilo.join()

print("Programa principal finalizado.")
