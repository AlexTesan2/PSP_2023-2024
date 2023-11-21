import threading
import time
import random

def tareaUno():
  global Realizado
  #time.sleep (random.random())
  print(Realizado)
  if not Realizado:
    print("Tarea realizada")  
    Realizado = True    
  return

Realizado = False
t = threading.Thread(target=tareaUno) # print("Tarea realizada") Realizado = True
t.start()
tareaUno() # no imprime nada Realizado = True
time.sleep(1)
