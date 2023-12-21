# events that cause interruption in program

try:
    num = input("enter a num")
    print(int(num))
except ValueError as e:
    print(e)
    print("enter only no.")
except Exception:
    print("something went wrong")
else:
    print("error out of global scope")
finally:
    print("closing program")