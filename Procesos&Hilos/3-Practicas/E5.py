"""
Using the multithreading module, write a simple python program as follows:
● Create a pool of threads to run concurrent tasks.
● The pool size should be 10.
● The thread should receive as input a number [id] (unique identifier for each of the
threads, starting from 1) and a number [number_of_writtings] (number of times the
thread will write the message).
● Each thread should sleep a random amount of time (between 100 and 300
milliseconds) and write the message ("I am 1", "I am 2", etc) a random number of times
between 5 and 15.
"""

import concurrent.futures
import threading
import random
import time

def worker_thread(thread_id, number_of_writings):
    sleep_time = random.uniform(0.1, 0.3) 
    write_count = random.randint(5, 15) 

    time.sleep(sleep_time)

    for i in range(1, write_count + 1):
        print(f"I am {thread_id}: Message {i} ({number_of_writings} total)")

def main():
    pool_size = 10

    with concurrent.futures.ThreadPoolExecutor(max_workers=pool_size) as executor:
        # Submitting tasks to the pool
        future_to_id = {executor.submit(worker_thread, i, random.randint(1, 100)): i for i in range(1, pool_size + 1)}

        # Waiting for all threads to complete
        for future in concurrent.futures.as_completed(future_to_id):
            thread_id = future_to_id[future]
            try:
                future.result()
            except Exception as e:
                print(f"Thread {thread_id} generated an exception: {e}")

if __name__ == "__main__":
    main()
