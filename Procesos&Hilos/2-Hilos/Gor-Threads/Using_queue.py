import time
import threading
import random
import queue

class Producer(threading.Thread):
    def __init__(self, queuee):
        threading.Thread.__init__(self)
        self.queuee = queuee
    
    def run(self):
        while True:
            integer = random.randint(0, 256)
            self.queuee.put(integer) 
            print("%d put to queuee by %s" % (integer, self.name))
            time.sleep(1)

class Consumer(threading.Thread):
    def __init__(self, queuee):
        threading.Thread.__init__(self)
        self.queuee = queuee
    
    def run(self):
        while True:
            integer = self.queuee.get()
            print("%d popped from list by %s" % (integer, self.name))
            self.queuee.task_done()

def main():
    queuee = queue.Queue()
    t1 = Producer(queuee)
    t2 = Consumer(queuee)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()

"""
Un hilo hace de productor y otro de consumidor,
el productor añade nums a la cola, 
el consumidor los quita,
la cola al ser queue, es comun para los dos hilos
"""