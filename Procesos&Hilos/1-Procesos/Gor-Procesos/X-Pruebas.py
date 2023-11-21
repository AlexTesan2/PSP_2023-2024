from multiprocessing import Process

def funcion(num):
    print ('hello world', num)

if __name__ == '__main__':
    for num in range(100):
        Process(target=funcion, args=(num,)).start()

"""
import os
print("hola")
print(os.cpu_count())

"""