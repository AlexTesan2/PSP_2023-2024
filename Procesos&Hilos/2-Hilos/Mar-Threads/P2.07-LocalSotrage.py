import threading  #no examen
import random
"""
The purpose of this code is to demonstrate how thread-local storage 
can be used to store data that is specific to each thread. 
Each thread has its own "copy" of the almacen object, 
and can set and get its value independently of the other threads.
"""
def mostrar(almacen):
  try:
    val = almacen.valor
  except AttributeError:
    print(f"Secondary {threading.current_thread().name}: Aún no inicializado dato del almacen\n", end="")
  else:
    print(f"{threading.current_thread().name}: {val}\n", end="")

def hilo(almacen):
  mostrar(almacen)
  almacen.valor = random.randint(1, 100)
  mostrar(almacen)



almacen = threading.local() #storage local a cada hilo
#almacen = threading.local()  hay un almacen != por hilo

#threading.local()  != almacen=local()  todos los hilos compartiran el mismo almacen

#Main thread
mostrar(almacen)
almacen.valor = 999
mostrar(almacen)

print('------------------Ahora los hijos----------\n')

#Hilos
for i in range(3):
  t = threading.Thread(target=hilo, args=(almacen,))
  t.start()


#si la info fuera comun para todos, el valor de llaves en el primer hilo seria 999
# threading.local() los datos q guarda un hilo en el almacen solo estaran disponibles para ese hilo
#get solo recupera la la info del hilo en el que se encuentra (thread in local)