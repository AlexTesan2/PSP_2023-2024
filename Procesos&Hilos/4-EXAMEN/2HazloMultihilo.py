"""
dado el siguiente código hazlo multihilo(0,5 puntos), 
consigue que la información pueda aparecer ordenada por pantalla y en el fichero se 
escriba de manera ordenada(2 puntos)

file_name = os.path.join(tempfile.gettempdir(), os.urandom(24).hex())

def code(name):
    time.sleep(10)
    with open(file_name, 'w') as f:
            print("guardando en "+file_name)
            f.write("codigo limpio fue escrito por "+str(name)) 
    subprocess.run(["ping", "google.com"])

LIMITAR EL PING A 4 toques
ping -c 4


OPCIONAL +0,5: ¿Qué mecanismo de los estudiados te permitiría sincronizar la muerte de P1?
Describe  todo lo que se te ocurra al respecto  El pool.map sincronizaria mejor
"""


import os
import subprocess
import tempfile
import threading
import time

lock = threading.Lock()

def code(name):
    time.sleep(10)

    with lock:
        print(f"Escribiendo en pantalla: Código limpio fue escrito por {name}")

    with open(file_name, 'a') as f:
        with lock:
            print(f"Escribiendo en archivo: Código limpio fue escrito por {name}")
            f.write(f"Código limpio fue escrito por {name}\n")

    ping_command = ["ping", "-c", "4", "google.com"]
    subprocess.run(ping_command)

if __name__ == "__main__":
    listaHilos = []
    file_name = os.path.join(tempfile.gettempdir(), os.urandom(24).hex())

    for i in range(5):
        thread = threading.Thread(target=code, args=(i,))
        listaHilos.append(thread)

    for thread in listaHilos:
        thread.start()
    for thread in listaHilos:
        thread.join()

    print("Proceso principal finalizado")

