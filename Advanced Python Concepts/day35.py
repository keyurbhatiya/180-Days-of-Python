# Day 35: Multithreading and Multiprocessing  

'''''
'''

# Multithreading

''''
Multithreading involves running multiple threads within the same process. Threads share the same memory space.
'''

# example
import threading

def print_numbers():
    for i in range(5):
        print(i)

# Creating threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_numbers)

# Starting threads
thread1.start()
thread2.start()

# Waiting for threads to finish
thread1.join()
thread2.join()


# Multiprocessing
'''
Multiprocessing creates separate processes, each with its own memory space. This allows true parallelism.
'''

# import multiprocessing

# def print_numbers():
#     for i in range(5):
#         print(i)

# # Creating processes
# process1 = multiprocessing.Process(target=print_numbers)
# process2 = multiprocessing.Process(target=print_numbers)

# # Starting processes
# process1.start()
# process2.start()

# # Waiting for processes to finish
# process1.join()
# process2.join()