# fork solo funciona en unix/macos
import os


def padre():
   while True:
      newpid = os.fork()
      if newpid == 0:
         # Este código se ejecuta en el proceso hijo
         hijo()
      else:
         # Este código se ejecuta en el proceso padre
         pids = (os.getpid(), newpid)
         print("Padre: %d, Hijo: %d\n" % pids)
      
      reply = input("Pulsa 's' si quieres crear un nuevo proceso")
      if reply != 's': 
         break

def hijo():
   print('\n>>>>>>>>>> Nuevo hijo creado con el pid %d a punto de finalizar<<<<<' % os.getpid())
   os._exit(0)  

padre()



# crea un nuevo proceso duplicando el proceso actual. Después de llamar a fork(),
# hay dos procesos idénticos que se están ejecutando, el proceso padre y el proceso hijo.