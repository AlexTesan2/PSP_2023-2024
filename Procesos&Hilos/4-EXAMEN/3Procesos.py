"""
EJERCICIO3(3 puntos + 0,5opcional)
Usando procesos, abre tres procesos,cada uno de los cuales debe….

	P1: debe abrir el bloc de notas/editor de texto del sistema que uses

	P2: debes esperar 5 segundos para cambiar la prioridad de P1

	P3: se lanza 2 segundos después de P2 haya arrancado y mata a P1 al instante

	¿Qué es lo que ocurre durante la ejecución?   El proceso 3 mata el bloc de notas antes de que el proceso dos le cambiee de prioridad 
    ¿Termina el programa correctamente?           Aunque el proceso mate al editor de texto, este no se cierra
    ¿Cómo podrías solucionarlo?                   Seguramente funcionara con el nanao de linux

OPCIONAL +0,5: 
¿Qué mecanismo de los estudiados te permitiría sincronizar
la muerte de P1?Describe  todo lo que se te ocurra al respecto 
"""

import os, psutil, time, subprocess, multiprocessing, sys
import cmd

def proceso1():
    print(f"Proceso1 con PID: {os.getpid()} creado.")
    subprocess.run(["notepad.exe"])

def proceso2():
    print(f"Proceso2 con PID: {os.getpid()} creado.")
    time.sleep(5)
    for proceso in psutil.process_iter(['pid', 'name']):
        #print(f"{proceso.info['pid']}, {proceso.info['name']}")
        if proceso.info['name'] == "notepad.exe" and int(proceso.info['pid']) != os.getpid():
            print("Bloc de notas encontrado")
            proceso.nice(8)
            print("Cambio de prioridad")

def proceso3():
    print(f"Proceso3 con PID: {os.getpid()} creado.")
    for proceso in psutil.process_iter(['pid', 'name']):
        #print(f"{proceso.info['pid']}, {proceso.info['name']}")
        if proceso.info['name'] == "notepad.exe" and int(proceso.info['pid']) != os.getpid():
            print("Bloc de notas encontrado y listo para ser eliminado")
            proceso.kill()
            print("eliminacion complletada")


if __name__ == "__main__":
    PROCESO_PADRE_PID = os.getpid()
    print(f"PROCESO_PADRE_PID= {PROCESO_PADRE_PID}")

    proceso_principal = multiprocessing.Process(name="proceso1",target=proceso1, args=())
    proceso_secundario = multiprocessing.Process(name="proceso2",target=proceso2, args=())
    proceso_terciario = multiprocessing.Process(name="proceso3",target=proceso3, args=())
    #proceso_principal = multiprocessing.Process(name="proceso1",target=proceso1, args=(PROCESO_PADRE_PID,))

    proceso_principal.start()
    proceso_secundario.start()
    time.sleep(2)
    proceso_terciario.start()
    proceso_principal.join()
    proceso_secundario.join()
    proceso_terciario.join()

    for proceso in psutil.process_iter(['pid', 'name']):
        if proceso.info['name'] == "notepad.exe" and int(proceso.info['pid']) != os.getpid():
            print("Bloc de notas encontrado al final")
        else:
            print("Bloc de notas NO  encontrado al final")

    print("Proceso principal finalizado")