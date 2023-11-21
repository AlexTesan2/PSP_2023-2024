import threading 

algo = 0

lock = threading.Lock() 

lock.acquire() 
algo +=1

lock.acquire()          #No puede haber un lock dentro de otro lock, se queda colgado
algo += 2
lock.release() 

print(algo) 