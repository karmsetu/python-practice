from mod2 import syahello
# ? if user is running this program as module or stand alone 

print(__name__)

syahello()

if __name__ == '__main__':
    print("main module")
else:
    print("a module")