"""
Using the multithreading module, write a python program as follows:
● Create a pool of threads to run concurrent tasks.
● The pool size should be 3.
● Create and fill an array of 100 random integer numbers.
● Run all 3 threads to parse the vector data. One of them must show the mean, another
the maximum and minimum value, and the last one the standard deviation. Note that
although these processes share the vector, they only do so for reading. None of them
must modify any value of the vector.
"""

import threading
import random
import numpy as np
import statistics

# Global variables
vector_lock = threading.Lock()
data_vector = [random.randint(1, 100) for _ in range(100)]

def calculate_mean():
    with vector_lock:
        mean = np.mean(data_vector)
    print(f"Mean: {mean}")

def calculate_min_max():
    with vector_lock:
        minimum = min(data_vector)
        maximum = max(data_vector)
    print(f"Minimum: {minimum}, Maximum: {maximum}")

def calculate_std_dev():
    with vector_lock:
        std_dev = statistics.stdev(data_vector)
    print(f"Standard Deviation: {std_dev}")

def main():
    thread_mean = threading.Thread(target=calculate_mean)
    thread_min_max = threading.Thread(target=calculate_min_max)
    thread_std_dev = threading.Thread(target=calculate_std_dev)

    thread_mean.start()
    thread_min_max.start()
    thread_std_dev.start()

    thread_mean.join()
    thread_min_max.join()
    thread_std_dev.join()

if __name__ == "__main__":
    main()
