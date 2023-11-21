import threading 

algo = 0

rlock = threading.RLock() 

rlock.acquire() 
algo += 1

rlock.acquire()
algo += 2
rlock.release() 
rlock.release() 

print(algo) 

"""
Una solucion es el reentral lock (rlock), se puede pedir tantas eces como quieras,
pero debes liberarlo tantas veces como lo has pedido

NO EXAMEN
"""