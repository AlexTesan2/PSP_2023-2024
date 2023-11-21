from multiprocessing import Pool, TimeoutError
import time
import os

def f(x):
    return x*x

if __name__ == '__main__':
    pool = Pool(processes=os.cpu_count())   #representa un grupo de procesos. # start 4 worker processes/ 12

    #print (pool.map(f, 20))
    # print "[0, 1, 4,..., 81]"

    """La función map distribuye los elementos de la secuencia 
        entre los procesos en el grupo y recopila los resultados,
        espera una secuencia como su segundo argumento."""
    
    print (pool.map(f, range(10)))                     #en el mismo orden en el que se dan los datos



    # print same numbers in arbitrary order
    for i in pool.imap_unordered(f, range(10)):
        print(i)

    """imap_unordered no garantiza el orden de los resultados en la salida. 
        Los resultados se imprimen tan pronto como están disponibles"""


    res = pool.apply_async(f, (20,))     
    print (res.get(timeout=1))              

    """
    apply_async Aplica la función de manera asíncrona a un solo valor (20)
    La llamada asíncrona permite que el programa principal continúe ejecutándose
    mientras se realiza la llamada asincrónica.

    Se utiliza el método get del objeto AsyncResult para 
    obtener el resultado de la llamada asincrónica. 
    El parámetro timeout especifica el tiempo máximo 
    (en segundos) que se esperará para obtener el resultado.
    Si el resultado no está disponible dentro del tiempo especificado, 
    se generará una excepción TimeoutError.
    """


    res = pool.apply_async(os.getpid, ())
    print (res.get(timeout=1))              
    #El resultado será el ID del proceso en el que se ejecutó os.getpid()



    # lista de los ID de cuatro procesos

    multiple_results = [pool.apply_async(os.getpid, ()) for i in range(4)]
    print([res.get(timeout=1) for res in multiple_results])




    # descansar 10 segundos, si no se completa en 1 segundo, lanza error

    res = pool.apply_async(time.sleep, (10,))
    try:
        print(res.get(timeout=1))
    except TimeoutError:
        print ("We lacked patience and got a multiprocessing.TimeoutError")