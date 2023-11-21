import threading
'''
The purpose of this code is to demonstrate the basic usage of threads in Python. 
The Saludo function is executed in both the main thread and the new thread t. 
The order in which the two "hola" messages are printed depends on the scheduling 
of the threads by the operating system, and may not be the same every time the program is run.
'''
#método al que se va a aosciar el hilo
def Saludo():
  print ('hola thread')   #impresión en el hilo principal

t = threading.Thread(target=Saludo)
t.start()
print ("hola main")       #impresión en el hilo principal