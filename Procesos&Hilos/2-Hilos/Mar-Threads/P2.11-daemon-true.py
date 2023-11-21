from threading import *
import time

def hilo():				
  for i in range(10):
    print('Hilo Daemon')
    time.sleep(1)
  print('Terminando Hilo secundario')

t = Thread(target=hilo)
t.daemon = True
t.start()	

time.sleep(5)				
print('Terminando Hilo principal')

#al terminar el principal, los hilos daemon mueren