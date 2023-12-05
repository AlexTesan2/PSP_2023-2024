"""
Cree un programa que ejecute 10 hilos, cada uno de los cuales sumará 100 números 
aleatorios entre el 1 y el 1000. Muestre el resultado de cada hilo. Ganará el hilo
que consiga el número mas alto
"""

import threading
import random

result_lock = threading.Lock()
max_sum = 0

def sum_numbers(thread_id):
    global max_sum
    thread_sum = sum(random.randint(1, 1000) for _ in range(100))
    
    with result_lock:
        print(f"Thread {thread_id}: Sum = {thread_sum}")
        if thread_sum > max_sum:
            max_sum = thread_sum

def main():
    threads = []
    for i in range(1, 11):
        thread = threading.Thread(target=sum_numbers, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"\nThe winner is the thread with the highest sum: {max_sum}")

if __name__ == "__main__":
    main()
