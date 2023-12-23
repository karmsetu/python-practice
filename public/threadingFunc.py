
# ? thread: a flow of excution, like a seperate order of instructions
# ! GIL: Global Lock Interpretor
# ? cpu bound : multiprocessing
# ? i/o bound : threading


import threading
import time

# ? multithreading

def count():
    time.sleep(3)
    print("you counted")


def eat():
    time.sleep(7)
    print("you ate")

def study():
    time.sleep(4)
    print("you studied")  

x = threading.Thread(target=count)
x.start()
y = threading.Thread(target=study)
y.start()
z = threading.Thread(target=eat)
z.start()
# count()
# eat()
# study()
print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())

# ? thread synchronisation

x.join() #? connects to the main thread