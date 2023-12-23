import time


# ? EPOCH
print(time.ctime(0))

# ?local time
timeObj = time.localtime()
print(timeObj)
local = time.strftime("%B %d %Y %H:%M:%S", timeObj)
print(local)