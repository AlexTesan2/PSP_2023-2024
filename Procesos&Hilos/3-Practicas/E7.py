"""
Cree un hilo que genere números aleatorios entre 1 y 100 y los vaya insertando en una lista, 
y otro que recorra circularmente esa lista y sustituya los números terminados en cero por el 
valor -1. Un tercer hilo abortará los otros dos en el momento en el que la suma de los 
elementos de la lista supere el valor de 20000
"""

import threading
import random

number_list = []
abort_flag = False
list_lock = threading.Lock()

def generate_numbers():
    global number_list, abort_flag
    while not abort_flag:
        with list_lock:
            number = random.randint(1, 100)
            number_list.append(number)

def process_numbers():
    global number_list, abort_flag
    while not abort_flag:
        with list_lock:
            for i in range(len(number_list)):
                if number_list[i] % 10 == 0:
                    number_list[i] = -1

def check_sum():
    global number_list, abort_flag
    while sum(number_list) <= 20000 and not abort_flag:
        pass  
    abort_flag = True

def main():
    thread_generate = threading.Thread(target=generate_numbers)
    thread_process = threading.Thread(target=process_numbers)
    thread_check_sum = threading.Thread(target=check_sum)

    thread_generate.start()
    thread_process.start()
    thread_check_sum.start()

    thread_check_sum.join()

    thread_generate.join()
    thread_process.join()

    print("Final List:", number_list)

if __name__ == "__main__":
    main()
