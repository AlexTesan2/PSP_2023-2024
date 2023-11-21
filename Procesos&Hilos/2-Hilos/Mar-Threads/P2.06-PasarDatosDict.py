import logging
import threading
import time

def thread_Apellido(name, inicio=1, fin=1):
  for x in range(inicio, fin):
    print (f"{name} Rodríguez {str(x)} años\n",end="")


nombres = ["Julio", "Javier", "Eladio", "Jose", "Manuel"]
hilos = list()
for n in nombres:
  # variable n es un string, and n, is a tuple with one element
  t = threading.Thread(target=thread_Apellido, args=(n,), kwargs={'inicio':5, 'fin':8})
  hilos.append(t)
  t.start()