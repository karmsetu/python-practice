import threading
import time
# ? a thread that runs in background, not imp for program to run
# ex: background task, garbage collection, waiting for input

def timer():
    count = 0
    while True:
        time.sleep(1)
        count+=1
        print("logged in for :", count, "seconds")

x  = threading.Thread(target=timer, daemon=True)
x.start()
print(x.isDaemon())
# x.daemon(True) # change nature of thread dynamically
ans = input("do you wish to exit?") # ext input is necessary