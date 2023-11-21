import threading
import time
import random

def tareaUno():
  global Done  
  time.sleep (random.random())
  if not Done:
    time.sleep (random.random())
    print("Tarea realizada")  
    Done = True
  else :
    print ("tarea NO REALIZADA")  
  return

Done = False
hilos = list()
for i in range(8):
  t = threading.Thread(target=tareaUno)
  hilos.append(t)
  t.start()
tareaUno()
time.sleep(1)