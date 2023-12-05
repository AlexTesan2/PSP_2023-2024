import multiprocessing
import random
import string

random.seed(123)

def crea_frase(length, output):
    frase = ''.join(random.choice(
                        string.ascii_lowercase
                        + string.ascii_uppercase
                        + string.digits)
                    for i in range(length))
    output.put(frase)


if __name__ == "__main__":
    
    output = multiprocessing.Queue()

    processes = [multiprocessing.Process(target=crea_frase, args=(10, output)) for x in range(4)]

    for p in processes:
        p.start()
    for p in processes:
        p.join()    #El programa principal espera a que todos los procesos hijos terminen antes de continuar

    results = [output.get() for p in processes] #La función get() se utiliza para extraer elementos de la cola.
    print(results)


"""
La cola se utiliza para recopilar resultados de los procesos 
y permitir al proceso principal acceder a esos resultados una vez 
que los procesos hayan terminado.
"""